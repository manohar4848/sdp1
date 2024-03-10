from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password




# from smsproject.adminapp.models import Admin,Faculty,Student,Course

def demofunction(request):
    return HttpResponse("I AM MANOJ")
def demofunction1(request):
    return render(request,"index.html")
def homer(request):
    return render(request,"homepage.html")
def aboutfunction(request):
    return render(request,"about.html")
def loginfunction(request):
    return render(request,"login.html")
def contactfunction(request):
    return render(request,"contact.html")
def admin_home(request):
    return render(request, 'adminhome.html')

def facultylogin(request):
    return render(request,"facultylogin.html")
def studentlogin(request):
    return render(request,"studentlogin.html")






