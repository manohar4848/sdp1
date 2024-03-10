# adminapp/views.py
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
import smtplib

from .forms import AddFacultyForm
from .models import Admin, FacultyCourseMapping
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from .models import Admin,Course,Faculty,Student,otp
def adminh(request):
    auname=request.session["auname"]
    return render(request, "adminhome.html",{"adminuname":auname})
def adminhb(request):
    return render(request,"homepage.html")


from .models import Admin,otp

def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)
    if flag:
        print("Login Success")
        request.session["auname"]=adminuname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        msg="LOGIN FAIL"
        return render(request, "login.html",{"message":msg})
        # return HttpResponse("LOGIN FAIL")





def checkstudentlogin(request):
    sid=request.POST["sid"]
    pwd=request.POST["pwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    student = Student.objects.all()
    print(flag)
    if flag:
        print("Login Success")
        request.session["sid"]=sid
        return render(request,"studenthome.html",{"sid":sid,"studentdata":student})
    else:
        msg="LOGIN FAIL"
        return render(request, "studentlogin.html",{"message":msg})
        # return HttpResponse("LOGIN FAIL")

# def sh(request):
#     auname=request.session["auname"]
#     student = Student.objects.all()
#     count=Student.objects.count()
#     return render(request,"studenthome.html",{"studentdata":student,"count":count,"adminuname":auname})
def viewstudent(request):
    auname=request.session["auname"]
    student = Student.objects.all()
    count=Student.objects.count()
    return render(request,"viewstudent.html",{"studentdata":student,"count":count,"adminuname":auname})
def viewfacutly(request):
    auname=request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})
def viewcourse(request):
    auname=request.session["auname"]
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursesdata":courses,"count":count,"adminuname":auname})

def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})
def admifaculty(request):
    auname=request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})
def admincourse(request):
    auname=request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})

def addcourse(request):
    auname=request.session["auname"]
    return render(request,"addcourse.html",{"adminuname":auname})

def insertcourse(request):
    if request.method=="POST":
        dept = request.POST["dept"]
        program = request.POST["program"]
        ay = request.POST["ay"]
        sem = request.POST["sem"]
        year = request.POST["year"]
        ccode = request.POST["ccode"]
        ctitle = request.POST["ctitle"]
        ltps=request.POST["ltps"]
        credits=request.POST["credits"]

        course=Course(department=dept,program=program,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
        Course.save(course)
        message="Course Added Successfully"
        return render(request,"addcourse.html",{"msg":message})
        # return HttpResponse("")

def deletecourse(request):
    auname=request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "deletecourse.html", {"coursesdata": courses, "count": count,"adminuname":auname})
    # return render(request,"deletecourse.html")
def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")
    # return HttpResponse("Course Deleted Successfully")

def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"courses":courses,"count":count})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})

def courseupdated(request):
    auname = request.session["auname"]
    cid=request.POST["cid"]
    courseid=int(cid)
    ctitle=request.POST["ctitle"]
    ltps=request.POST["ltps"]
    credits=request.POST["credits"]
    Course.objects.filter(id=courseid).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    msg="Course updated Successfully"
    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname,"cid":cid})






from django.shortcuts import render
from .forms import AddFacultyForm


def addfaculty(request):
    form = AddFacultyForm()
    auname=request.session["auname"]
    message = ""  # Initialize an empty message

    if request.method == 'POST':
        form1 = AddFacultyForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            message = "Faculty Added Successfully"
        else:
            message="Fail To add Faculty"

    return render(request, "addfaculty.html", {"form": form, "msg": message,"adminuname":auname})

from .forms import AddFacultyForm,AddStudentForm,AddfacultycoursemappingForm,StudentForm,FacultyForm
from .forms import AddStudentForm
from django.shortcuts import render

from .forms import AddStudentForm

def addstudent(request):
    form = AddStudentForm()
    auname=request.session["auname"]

    message = ""  # Initialize an empty message

    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Student Added Successfully"

        else:
            message="Fail to add student"

    return render(request, "addstudent.html", {"form": form, "msg": message,"adminuname":auname})


from django.shortcuts import render, redirect
def deletefaculty(request):
    auname=request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})
    # return render(request,"deletecourse.html")
def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")

def updatestudent(request):
    auname=request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "updatestudent.html", {"studentdata": student, "count": count,"adminuname":auname})
from django.contrib import messages

def studentupdation(request, sid):
    auname = request.session["auname"]
    student = get_object_or_404(Student, pk=sid)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect('updatestudent')  # Redirect to the same page after updating
        else:
            messages.error(request, "Updation Fail")
    else:
        form = StudentForm(instance=student)
    return render(request, "studentupdated.html", {"form": form, "adminuname": auname})

    return HttpResponse(sid)



def updatefaculty(request):
    auname=request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "updatefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})
from django.contrib import messages

def facultyupdation(request, fid):
    auname = request.session["auname"]
    faculty = get_object_or_404(Faculty, pk=fid)
    if request.method == "POST":
        form = FacultyForm(request.POST, request.FILES, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty updated successfully")
            return redirect('updatefaculty')  # Redirect to the same page after updating
        else:
            messages.error(request, "Updation Fail")
    else:
        form = FacultyForm(instance=faculty)
    return render(request, "facultyupdated.html", {"form": form, "adminuname": auname})

    return HttpResponse(fid)

def deletestudent(request):
    auname=request.session["auname"]
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentdata": student, "count": count,"adminuname":auname})
    # return render(request,"deletecourse.html")
def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")

def facultycoursemapping(request):
    fmcourses=FacultyCourseMapping.objects.all()
    auname=request.session["auname"]

    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses})
def adminchangepassword(request):
    auname=request.session["auname"]
    return render(request,"adminchangepassword.html",{"adminuname":auname})





import re
import smtplib
import random
from django.shortcuts import render
  # Import your OTPModel here

def is_valid_email(email):
    # Using regular expression to validate email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def sentotp(request):
    if request.method == 'POST':
        fullname = request.POST.get("name1")
        email = request.POST.get("email")

        # Generate a random 6-digit OTP
        ot = random.randint(100000, 999999)

        # Validate the email format
        if not is_valid_email(email):
            return render(request, "invalid_email.html")

        # Setting up SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        password = "wgkdfzapygmzqakm"  # Assuming this is the password for manojkadambala2005@gmail.com
        server.login("manojkadambala2005@gmail.com", password)

        # Send OTP email
        body = f"Dear {fullname},\n\nYour OTP is: {ot}."
        subject = "OTP verification using Python"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail("manojkadambala2005@gmail.com", email, message)

        # Save OTP details to the database
        otp_instance = otp(fullname=fullname, email=email, ot=ot)
        otp_instance.save()

        return render(request, "verifyotp.html", {'email': email})

    return render(request, "sendotp.html")

def verifyotp(request):
    adminuname=request.POST["name1"]
    admail=request.POST["email"]
    op=request.POST["otp"]

    flag=otp.objects.filter(Q(email=admail)&Q(ot=op))
    print(flag)
    if flag:
        print("Login Success")
        request.session["auname"]=adminuname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        msg="LOGIN FAIL"
        return render(request, "verifyotp.html",{"message":msg})

def adminupdatepwd(request):
    auname=request.session["auname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("old is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated")
        msg="Password Updated Successfully"
    else:
        print("Old password invalid")
        msg=" Old Password is incorrect"
    return render(request,"adminchangepassword.html",{"adminuname":auname,"message":msg})

def addfacultycoursemapping(request):
    form = AddfacultycoursemappingForm()
    auname=request.session["auname"]
    message = ""  # Initialize an empty message

    if request.method == 'POST':
        form1 = AddfacultycoursemappingForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            message = "FacultyCoursemapping Added Successfully"
        else:
            message="Fail To add FacultyCoursemapping"

    return render(request, "addfacultycoursemapping.html", {"form": form, "msg": message,"adminuname":auname})
