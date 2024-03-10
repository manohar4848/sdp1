# adminapp/urls.py
from django.urls import path
from . import views
from .views import otp


urlpatterns = [
    path('adm/', views.adminh, name="adm"),  # Update the path to 'adm/' instead of 'a/'
    # path('adminlogout/', views.admin_logout, name='adminlogout'),
    path('hb/', views.adminh, name="adminhb"),
    # path('checkadminlogin/', views.checkadminlogin, name='checkadminlogin'),
    path('checkadminlogin/', views.checkadminlogin, name='checkadminlogin'),
    # path('checkstudentlogin/',views.checkstudentlogin,name='checkstudentlogin'),

    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('adminstudent/', views.adminstudent, name='adminstudent'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('deletestudent',views.deletestudent,name="deletestudent"),
    path('studentdeletion/<int:sid>/', views.studentdeletion, name="studentdeletion"),
    path('updatestudent',views.updatestudent,name="updatestudent"),
    path('studentupdation/<int:sid>/',views.studentupdation,name="studentupdation"),

    path('updatefaculty',views.updatefaculty,name="updatefaculty"),
    path('facultyupdation/<int:fid>/',views.facultyupdation,name="facultyupdation"),
    path('viewfaculty/', views.viewfacutly, name='viewfaculty'),
    path('adminfaculty', views.admifaculty, name="adminfaculty"),

    # path('addfaculty/', views.addfaculty, name='addfaculty'),
    path('viewcourses/', views.viewcourse, name='viewcourses'),
    path('admincourse',views.admincourse,name='admincourse'),
    path('ad/addcourse/', views.addcourse, name='addcourse'),
    path('insertcourse',views.insertcourse,name="inseretcourse"),
    path('deletecourse',views.deletecourse,name="deletecourse"),
    path('coursedeletion/<int:cid>/', views.coursedeletion, name="coursedeletion"),
    path('updatecourse/',views.updatecourse,name="updatecourse"),
    path('courseupdation/<int:cid>/',views.courseupdation,name="courseupdation"),
    path('courseupdated/',views.courseupdated,name="courseupdated"),
    # ... other patterns if any

    # path('addfaculty/', views.addfaculty, name='addfaculty'),
    path('addfaculty/', views.addfaculty, name='addfaculty'),
    path('addfacultycoursemapping/',views.addfacultycoursemapping,name="addfacultycoursemapping"),
    path('adm/', views.adminh, name="adm"),  # Update the path to 'adm/' instead of 'a/'
    path('deletefaculty',views.deletefaculty,name="deletefaculty"),
    path('facultydeletion/<int:fid>/', views.facultydeletion, name="facultydeletion"),
    path('facultycoursemapping',views.facultycoursemapping,name="facultycoursemapping"),
    path('adminchangepassword',views.adminchangepassword,name="adminchangepassword"),
    path('adminupdatepwd',views.adminupdatepwd,name="adminupdatepwd"),

    path('otp/',views.sentotp, name='otp'),
    path('vo/',views.verifyotp,name="vo")


]
