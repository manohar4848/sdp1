from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Faculty,Course,FacultyCourseMapping

# from smsproject.facultyapp.forms import AddCourseContentForm
from .forms import AddCourseContentForm


# Create your views here.
def facultyhome(request):
    fid = request.session["fid"]
    faculty = Faculty.objects.get(facultyid=fid)
    faculty_image = faculty.image
    return render(request, "facultyhome.html", {"fid": fid, "faculty": faculty, "faculty_image": faculty_image})

def checkfacultylogin(request):
    fid=request.POST["fid"]
    pwd=request.POST["pwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))
    print(flag)
    if flag:
        print("Login Success")
        faculty = Faculty.objects.get(facultyid=fid)
        faculty_image = faculty.image

        request.session["fid"]=fid
        return render(request,"facultyhome.html",{"fid":fid,"faculty":faculty,"faculty_image":faculty_image})
    else:
        msg="LOGIN FAIL"
        return render(request, "facultylogin.html",{"message":msg})
        # return HttpResponse("LOGIN FAIL")

def facultycourses(request):
    fid = request.session["fid"]
    print(fid)
    courses=Course.objects.all()
    count=Course.objects.count()
    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        # print(type(course.faculty.facultyid))
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)
    print(fmcourses)
    dir(fmcourses)
    count=len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})

def facultychangepassword(request):
    fid=request.session["fid"]
    return render(request,"facultychangepassword.html",{"fid":fid})

def facultyupdatepwd(request):
    fid=request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("old is correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("updated")
        msg="Password Updated Successfully"
    else:
        print("Old password invalid")
        msg=" Old Password is incorrect"
    return render(request,"facultychangepassword.html",{"fid":fid,"message":msg})

def addcoursecontent(request):
    form = AddCourseContentForm()
    auname=request.session["auname"]
    message = ""  # Initialize an empty message

    if request.method == 'POST':
        form1 = AddCourseContentForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            message = "CourseContent Added Successfully"
        else:
            message="Fail To add CourseContent"

    return render(request, "addcoursecontent.html", {"form": form, "msg": message,"adminuname":auname})