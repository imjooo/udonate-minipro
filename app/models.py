from datetime import date
from distutils.command.upload import upload
import email
from re import sub
from time import time
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class login (models.Model):
    log_id=models.AutoField(primary_key=True)
    username=models.CharField("username",max_length=100)
    password=models.CharField("password",max_length=100)
    role=models.CharField("role",max_length=50)

class donor(models.Model):
    user_id=models.AutoField(primary_key=True)
    fname=models.CharField("fname",max_length=100) 
    lname=models.CharField("lname",max_length=100)  
    DOB=models.DateField("dob",max_length=100)
    gender=models.CharField("gender",max_length=100)
    email=models.CharField("email",max_length=100)
    ph_no=models.CharField("phn_no",max_length=100)
    blood_grp=models.CharField("blood_grp",max_length=100)
    medical_certificate=models.FileField("medical_certificate",max_length=100,upload_to="images/")
    last_donate=models.CharField("last_donate",max_length=100)
    district=models.CharField("district",max_length=100) 
    status=models.CharField("status",max_length=100)
    
    logid=models.ForeignKey(login,on_delete=models.CASCADE,null=True)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    fname=models.CharField("fname",max_length=100) 
    lname=models.CharField("lname",max_length=100)  
    DOB=models.DateField("dob",max_length=100)
    gender=models.CharField("gender",max_length=100)
    email=models.CharField("email",max_length=100)
    ph_no=models.CharField("phn_no",max_length=100)
    status=models.CharField("status",max_length=100)
    logid=models.ForeignKey(login,on_delete=models.CASCADE,null=True)

class hospital(models.Model):
    hid= models.AutoField(primary_key=True)
    hname= models.CharField("Name",max_length=100)
    address = models.CharField("address", max_length=500)
    phone=models.CharField("phone",max_length=100)
    logid=models.ForeignKey(login, on_delete=models.CASCADE, null=True)
    email=models.CharField("email",max_length=50)

class booked(models.Model):
    book_id= models.AutoField(primary_key=True)
    don=models.ForeignKey(donor, on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    date=models.CharField("date",max_length=100)
    status=models.CharField("status",max_length=100)

class notifications(models.Model):
    not_id=models.AutoField(primary_key=True)
    name=models.CharField("name",max_length=100)
    description=models.CharField("description",max_length=300)
    date=models.DateField("date",max_length=100)
    time=models.CharField("time",max_length=100)


class complaints(models.Model):
    comp_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    sub=models.CharField("sub",max_length=100)
    msg=models.CharField("msg",max_length=100)
    reply=models.CharField("reply",max_length=100)

class donor_complaints(models.Model):
    comp_id=models.AutoField(primary_key=True)
    donor=models.ForeignKey(donor, on_delete=models.CASCADE, null=True)
    sub=models.CharField("sub",max_length=100)
    msg=models.CharField("msg",max_length=100)
    reply=models.CharField("reply",max_length=100)

class hosp_complaints(models.Model):
    comp_id=models.AutoField(primary_key=True)
    hospital=models.ForeignKey(hospital, on_delete=models.CASCADE, null=True)
    sub=models.CharField("sub",max_length=100)
    msg=models.CharField("msg",max_length=100)
    reply=models.CharField("reply",max_length=100)



