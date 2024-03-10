from django.urls import path
from . import views
urlpatterns = [
    path('checkstudentlogin/', views.checkstudentlogin, name='checkstudentlogin'),
    path('studenthome/',views.studenthome,name="studenthome"),
    path('studentchangepassword', views.studentchangepassword, name="studentchangepassword"),
    path('studentupdatepwd', views.studentupdatepwd, name="studentupdatepwd"),
    path('studentcourses',views.studentcourses,name="studentcourses"),
    path('displaystudentcourses',views.displaystudentcourses,name="displaystudentcourses"),
    path('studentcoursecontent',views.studentcoursecontent,name="studentcoursecontent"),
]