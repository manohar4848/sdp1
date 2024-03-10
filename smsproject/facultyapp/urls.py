from django.urls import path
from . import views
urlpatterns = [
    path('checkfacultylogin/', views.checkfacultylogin, name='checkfacultylogin'),
    path('facultyhome/',views.facultyhome,name="facultyhome"),
    path('facultycourses/',views.facultycourses,name="facultycourses"),
    path('facultychangepassword',views.facultychangepassword,name="facultychangepassword"),
    path('facultyupdatepwd',views.facultyupdatepwd,name="facultyupdatepwd"),
    path('addcoursecontent',views.addcoursecontent,name="addcoursecontent"),
]