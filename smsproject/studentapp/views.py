from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course
from facultyapp.models import CourseContent

# Create your views here.
def studenthome(request):
    sid=request.session["sid"]
    student = Student.objects.get(studentid=sid)
    student_image = student.image
    return render(request, "studenthome.html", {"sid": sid, "student": student, "student_image": student_image})
    # sid=request.session["sid"]

    # return render(request,"studenthome.html",{"studentdata":student,"count":count,"adminuname":sid})
# views.py

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]
    flag = Student.objects.filter(Q(studentid=sid) & Q(password=pwd))

    if flag:
        print("Login Success")
        # Fetch the student object
        student = Student.objects.get(studentid=sid)
        # Get the image associated with the student
        student_image = student.image
        request.session["sid"] = sid
        return render(request, "studenthome.html", {"sid": sid, "student": student, "student_image": student_image})
    else:
        msg = "LOGIN FAIL"
        return render(request, "studentlogin.html", {"message": msg})


def studentchangepassword(request):
    sid=request.session["sid"]
    return render(request,"studentchangepassword.html",{"sid":sid})

def studentupdatepwd(request):
    sid=request.session["sid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("old is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated")
        msg="Password Updated Successfully"
    else:
        print("Old password invalid")
        msg=" Old Password is incorrect"
    return render(request,"studentchangepassword.html",{"sid":sid,"message":msg})

def studentcourses(request):
    sid=request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid=request.session["sid"]
    content=CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})
def displaystudentcourses(request):
    ay=request.POST["ay"]
    sem=request.POST["sem"]
    sid = request.session["sid"]

    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})
# def viewstudent(request):
#     sid=request.session["sid"]
#     student = Student.objects.filter(Q(studentid=sid))
#     count=Student.objects.count()
#     return render(request,"viewstudent.html",{"studentdata":student,"count":count,"adminuname":auname})