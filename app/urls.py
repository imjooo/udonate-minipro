from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
   path('',views.index,name='index'),
   path('index',views.index,name='index'),
   path('registration',views.registration,name='registration'),
   path('usereg',views.usereg,name='usereg'),
   path('search',views.search,name='search'),
   path("donor",views.donor,name="donor"),
   path('admin',views.admin,name='admin'),
   path('user1',views.user1,name='user1'),
   path("donor1",views.donor1,name="donor1"),
   path('hospital',views.hospital,name='hospital'),
   path("logup",views.logup,name="logup"),
   path("events",views.events,name="events"),
   path("message",views.message,name="message"),
   path("listuser",views.listuser,name="listuser"),
   path("listdonor",views.listdonor,name="listdonor"),
   path("hospital",views.hospital,name="hospital"),
   path("add_hospital",views.add_hospital,name="add_hospital"),
   path("add_hospital1",views.add_hospital1,name="add_hospital1"),
   path("logout",views.logout,name="logout"),
   path("Privacy",views.Privacy,name="Privacy"),
   path("listhospital",views.listhospital,name="listhospital"),
   path("remove_usr",views.remove_usr,name='remove_usr'),
   path("searchblood",views.searchblood,name="searchblood"),
   path('requestblood',views.requestblood,name="requestblood"),   
   path("listdonorhsptl",views.listdonorhsptl,name="listdonorhsptl"),
   path("approveuser",views.approveuser,name="approveuser"),
   path("rejectuser",views.rejectuser,name="rejectuser"),
   path("requesteddonor",views.requesteddonor,name="requesteddonor"),
   path("user",views.user,name="user"),
   path("remove_hosp",views.remove_hosp,name="remove_hosp"),
   path("remove_user",views.remove_user,name="remove_user"),
   path("approveddonor",views.approveddonor,name="approveddonor"),
   path("accepted1",views.accepted1,name="accepted1"),
   path("notification",views.notification,name="notification"),
   path("complaints",views.complaints,name="complaints"),
   path("usercomplaint",views.usercomplaint,name="usercomplaint"),
   path("donorcomplaint",views.donorcomplaint,name="donorcomplaint"),
   path("donor_complaints",views.donor_complaints,name="donor_complaints"),
   path("hospitalcomplaint",views.hospitalcomplaint,name="hospitalcomplaint"),
   path("hospital_complaints",views.hospital_complaints,name="hospital_complaints"),
   path("notification_accepted",views.notification_accepted,name="notification_accepted"),
   path("ursmsg_list",views.ursmsg_list,name="ursmsg_list"),
   path("donmsg_list",views.donmsg_list,name="donmsg_list"),
   path("hospmsg_list",views.hospmsg_list,name="hospmsg_list"),
   path("adminmsg",views.adminmsg,name="adminmsg"),
   path("remove_msg",views.remove_msg,name="remove_msg"),
]
if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
