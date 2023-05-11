import email
from urllib import request
from django.shortcuts import render,redirect
from .models import donor as don,login as log,hospital as hosp, booked as book,user as usr,notifications as notif,donor_complaints as dcm,complaints as cm,hosp_complaints as hcm
from datetime import date

# Create your views here.

def index(request):
    return render(request,'index.html')
def registration(request):
    return render(request,'registration.html')
def search(request):
    return render(request,'search.html')
def usereg(request):
    return render(request,'usereg.html')
def message(request):
    return render(request,'messages.html')
def donor(request):
    if request.POST:
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        DOB=request.POST["DOB"]
        gender=request.POST["gender"]
        email=request.POST["email"]
        ph_no=request.POST["ph_no"]
        blood_grp=request.POST["blood_grp"]
        district=request.POST["district"]
        medical_certificate=request.FILES["medical_certificate"]
        last_donate=request.POST["last_donate"]
        username=request.POST["username"]
        password=request.POST["password"]
        datau=log.objects.filter(username=username).count()
        if datau==1:
            response=redirect("/index?msg=username already exist")
            return response
        else:
            data=log.objects.create(username=username,password=password,role="donor")
            don.objects.create(logid=data,fname=fname,lname=lname,DOB=DOB,gender=gender,email=email,ph_no=ph_no,blood_grp=blood_grp,district=district,medical_certificate=medical_certificate,last_donate=last_donate,status="")
        response=redirect("/index")
        return response

def user(request):
    if request.POST:
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        DOB=request.POST["DOB"]
        gender=request.POST["gender"]
        email=request.POST["email"]
        ph_no=request.POST["ph_no"]
        username=request.POST["username"]
        password=request.POST["password"]
        datau=log.objects.filter(username=username).count()
        if datau==1:
            response=redirect('/index?msg=username already exist')
            return response
        else:
            data=log.objects.create(username=username,password=password,role="user")
            usr.objects.create(logid=data,fname=fname,lname=lname,DOB=DOB,gender=gender,email=email,ph_no=ph_no)
        response=redirect("/index")
        return response

def admin(request):
    return render(request,'adminhome.html')
def user1(request):
    return render(request,'userhome.html')
def donor1(request):
    return render(request,'donorhome.html')
def hospital(request):
    return render(request,'hospitalhome.html')

def user_complaints(request):
    return render(request,'complaints.html')
def donor_complaints(request):
    return render(request,'donorcomplaints.html')
def logup(request):
    msg=""
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        try:
            data = log.objects.get(username=user, password=password)
            
            if (data.role == "admin"):
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.log_id
                response = redirect('/admin?Login successful')
                return response
            elif (data.role == "hospital"):
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.log_id
                response = redirect('/hospital')
                return response
            elif(data.role =="donor"):
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.log_id
                response = redirect('/donor1')
                return response   
            elif(data.role =="user"):
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.log_id
                response = redirect('/user1')
                return response       
            else:
                return render(request, "index.html", {"msg": "invalid account Details"})
        except:
            return render(request, "index.html", {"msg": "invalid user name or password "})
    else:
        response = redirect('/index')
        return response

def listdonor(request):
    data=don.objects.filter(status="approved").all()
    return render(request,"donorlist.html",{"data":data})

def approveddonor(request):
    data=don.objects.filter(status="approved").all()
    return render(request,"approveddonor.html",{"data":data})

def listuser(request):
    data=usr.objects.filter(status="").all()
    return render(request,"userlist.html",{"data":data})

def listdonorhsptl(request):
    data=don.objects.filter(status="").all()
    return render(request,"useronhsptl.html",{"data":data})

def approveuser(request):
    id=request.POST['user_id']
    don.objects.filter(user_id=id).update(status="approved")
    response=redirect("/listdonorhsptl")
    return response

def rejectuser(request):
    id=request.POST['user_id']
    don.objects.filter(user_id=id).update(status="rejected")
    response=redirect("/listdonorhsptl")
    return response

def add_hospital(request):
    return render(request,"add_hospital.html")

def add_hospital1(request):
    if request.POST:
        hname=request.POST["hname"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        data=log.objects.create(username=username,password=password,role="hospital")
        hosp.objects.create(logid=data,hname=hname,address=address,phone=phone,email=email)
    response=redirect("/admin")
    return response

def logout(request):
    try:
        del request.session["id"]
        del request.session["role"]
        del request.session["username"]
        response=redirect("/index")
        return response
    except:
        response=redirect("/index")
        return response

def Privacy(request):
    msg=""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session["id"]
        data=log.objects.get(log_id=id)
        if data.password==t1:
            msg="sucessfully updated"
            log.objects.filter(log_id=id).update(password=t2)
        else:
            msg="invalid current password"

    returnpage="adminhead.html"
    if(request.session.get('role', ' ')=="hospital"):
        returnpage="staffhead.html"
    if(request.session.get('role', ' ')=="admin"):
        returnpage="adminhead.html"
    elif(request.session.get('role', ' ')=="health"):
        returnpage="userhead.html"
    return render(request, "privacy.html",{"role":returnpage,"msg":msg})

    
def remove_usr(request):
    don.objects.filter(user_id=request.GET["id"]).delete()
    response = redirect('/listdonor')
    return response

def remove_user(request):
    usr.objects.filter(user_id=request.GET["id"]).delete()
    response = redirect('/listuser')
    return response


def remove_hosp(request):
    hosp.objects.filter(hid=request.GET["id"]).delete()
    response = redirect('/listhospital')
    return response

def listhospital(request):
    data=hosp.objects.all()
    return render(request,"list_hospital.html",{"data":data})

def searchblood(request):
    id=request.session["id"]
    blood_grp=request.POST["blood_grp"]
    district=request.POST["district"]
    data=don.objects.filter(blood_grp=blood_grp,district=district,status="approved")
    return render(request,"searchlist.html",{"data":data})

def requestblood(request):
    id=request.POST['user_id']
    data=don.objects.get(user_id=id)
    userid=request.session["id"]
    datal=log.objects.get(log_id=userid)
    datau=usr.objects.get(logid=datal)
    dates=date.today()
    don.objects.filter(user_id=id).update(status="booked")
    book.objects.create(don=data,user=datau,date=dates,status="booked")
    response=redirect("/user1")
    return response

def requesteddonor(request):
    data=book.objects.filter(status="booked").all()
    return render(request,"request.html",{"data":data})

def accepted1(request):
    id=request.POST['user_id']
    book.objects.filter(user_id=id).update(status="approved")
    response=redirect("/user1")
    return response

def notification(request):
    data=book.objects.filter(status="approved").all()
    return render(request,"notification.html",{"data":data})

def notification_accepted(request):
    data=book.objects.filter(status="approved").all()
    return render(request,"notification_accepted.html",{"data":data})

def donor_complaints(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        dcm.objects.filter(comp_id=t1).update(reply=t2)
    data=dcm.objects.all()
    return render(request,"donor_feed.html",{"data":data})

def donorcomplaint(request):
    id=request.session["id"]
    data1=log.objects.get(log_id=id)
    datas=don.objects.get(logid=data1)
    if request.POST:
        t1=request.POST["subject"]
        t2=request.POST["msg"]
        dcm.objects.create(donor=datas,sub=t1,msg=t2,reply="")
    data=dcm.objects.filter(donor=datas).all()
    return render(request,"donorcomplaints.html",{"data":data})

def usercomplaint(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        cm.objects.filter(comp_id=t1).update(reply=t2)
    data=cm.objects.all()
    return render(request,"adminfeed.html",{"data":data})

def complaints(request):
    id=request.session["id"]
    data1=log.objects.get(log_id=id)
    datas=usr.objects.get(logid=data1)
    if request.POST:
        t1=request.POST["subject"]
        t2=request.POST["msg"]
        cm.objects.create(user=datas,sub=t1,msg=t2,reply="")
    data=cm.objects.filter(user=datas).all()
    return render(request,"complaints.html",{"data":data})

def hospital_complaints(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        hcm.objects.filter(comp_id=t1).update(reply=t2)
    data=hcm.objects.all()
    return render(request,"hospital_feed.html",{"data":data})

def hospitalcomplaint(request):
    id=request.session["id"]
    data1=log.objects.get(log_id=id)
    datas=hosp.objects.get(logid=data1)
    if request.POST:
        t1=request.POST["subject"]
        t2=request.POST["msg"]
        hcm.objects.create(hospital=datas,sub=t1,msg=t2,reply="")
    data=hcm.objects.filter(hospital=datas).all()
    return render(request,"hospitalcomplaints.html",{"data":data})

def events(request):
    if request.POST:
        name=request.POST["name"]
        description=request.POST["description"]
        date=request.POST["date"]
        time=request.POST["time"]
        
        notif.objects.create(name=name,description=description,date=date,time=time)
    response=redirect("/admin")
    return response

def ursmsg_list(request):
    data=notif.objects.all()
    return render(request,"usermsg.html",{"data":data})

def donmsg_list(request):
    data=notif.objects.all()
    return render(request,"donormsg.html",{"data":data})

def hospmsg_list(request):
    data=notif.objects.all()
    return render(request,"hospmsg.html",{"data":data})

def adminmsg(request):
    data=notif.objects.all()
    return render(request,"adminmsg.html",{"data":data})

def remove_msg(request):
    notif.objects.filter(not_id=request.GET["id"]).delete()
    response = redirect('/adminmsg')
    return response

