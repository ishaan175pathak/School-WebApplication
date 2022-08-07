from dataclasses import dataclass
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import get_list_or_404, render,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializer import *
# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request,"index.html")

def login(request):
        if request.method == "GET":
            return render(request,"login.html")

        elif request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]

            for dat in Register.objects.all():
                if dat.email == email and dat.password == password:
                    if dat.authority == "faculty":
                        return HttpResponseRedirect(f"../classroom/faculty/{dat.name}/")

                    elif dat.authority == "student":
                        return HttpResponseRedirect(f"../classroom/student/{dat.name}/")

                    elif dat.authority == "hod":
                        return HttpResponseRedirect(f"../classroom/hod/")
            else:
                return render(request,"login.html",{"message":"Login Credentials Failed !","class":"alert alert-danger"})

def Logout(request):
    logout(request)

    return HttpResponseRedirect("/login/")

def classroom_faculty(request,name):
    info = get_object_or_404(Register,name=name)
    alldata = Allotment.objects.filter(name=name)
    faculty_data=Faculty.objects.all()
    student_data = []

    for dat in alldata:
        for stu_info in Student.objects.all():
            if dat.Class == stu_info.Class and dat.section == stu_info.section:
                student_data.append(stu_info.regis.name)

    if request.method == "GET":
        return render(request,"faculty/classroom_faculty.html",{"information":info,"data":alldata,"receive_faculty":faculty_data,"receive_student":student_data})
    elif request.method == "POST":
        pass

def classroom_faculty_queries(request,name):
    data = get_object_or_404(Register,name=name)

    if request.method == "GET":
        return render(request,"faculty/classroom_faculty_queries.html",{"information":data})

    elif request.method == "POST":
        pass

def notice(request,name):
    rd = get_object_or_404(Register,name=name)
    allot = Allotment.objects.filter(name=name)
    if request.method == "GET":
        return render(request,"faculty/notice.html",{"information":rd,"allot":allot})

    elif request.method == "POST":
        name  = request.POST["sname"]
        Class = request.POST["Class"]
        section = request.POST["section"]
        message = request.POST["notice"]
    
        nobj = Notice(name=name,Class=Class,section=section,notice=message)

        try:
            nobj.save()
            return render(request,"faculty/notice.html",{"information":rd,"message":"Saved Notice Successfully","class":"alert alert-success"})
        except:
            return render(request,"faculty/notice.html",{"information":rd,"message":"Error Occured !! ","class":"alert alert-danger"})


def studentEnroll(request,name):
    finfo = get_object_or_404(Register,name=name)
    if request.method == "GET":
        return render(request,"faculty/StudentEnroll.html",{"information":finfo})
    
    elif request.method == "POST":
        sname = request.POST["name"]
        authority = "student"
        email  = request.POST["email"]
        password  = request.POST["password"]
        address  = request.POST["address"]
        phoneNumber  = request.POST["phone"]
        Class  = request.POST["sem"]
        section = request.POST["section"]


        regisObj = Register(name=sname,authority=authority,email=email,password=password,address=address,phone=phoneNumber)
        sobj = Student(regis=regisObj,Class=Class,section=section)
        try:
            regisObj.save()
            sobj.save()
            return render(request,"faculty/StudentEnroll.html",{"information":finfo,"message":"Student SuccessFully Enrolled","class":"alert alert-success"})
        except:
            return render(request,"faculty/StudentEnroll.html",{"information":finfo,"message":"Try Again","class":"alert alert-danger"})

# Going to create a rest API for viewing the content of the Answers

def submission(request,name):
    info = get_object_or_404(Register,name=name)
    if request.method == "GET":
        return render(request,"faculty/viewSubmission.html",{"information":info})

def make_assignment(request,name):
    rinfo = get_object_or_404(Register,name=name)
    ainfo = Allotment.objects.filter(name=name)

    if request.method == "GET":
        return render(request,"faculty/make_assignment.html",{"information":rinfo,"faculty_info":ainfo})        
        
    elif request.method == "POST":
        Class  = request.POST["class"]
        section = request.POST["section"] 
        topic = request.POST["topic"]

        qobj = Questions(teacher=name,Class=Class,section=section,question=topic)

        try:
            qobj.save()
            return render(request,"faculty/make_assignment.html",{"information":rinfo,"faculty_info":ainfo,"message":"Assignment Created successfully !!","class":"alert alert-success"})
        except:
            return render(request,"faculty/make_assignment.html",{"information":rinfo,"faculty_info":ainfo,"message":"Error Occured while creating Assignment !!","class":"alert alert-danger"})

def hod(request):
    if request.method == "GET":
        data = Allotment.objects.all()
        return render(request,"hod/principal.html",{"data":data})

    elif request.method == "POST":
        pass

def allotment(request):
    data = Register.objects.filter(authority="faculty")

    if request.method == "GET":
        return render(request,"hod/allotment.html",{"data":data})

    elif request.method == "POST":

        name = request.POST["name"]
        Class = request.POST["class"]
        section = request.POST["section"]
        subject = request.POST["subject"]

        obj = Allotment(name=name,Class=Class,section=section,subject=subject)

        try:
            obj.save()
            return render(request,"hod/allotment.html",{"data":data,"message":"Allotment Successful","class":"alert alert-success"})
        except:
            return render(request,"hod/allotment.html",{"data":data,"message":"Try again","class":"alert alert-danger"})

def facultyEnroll(request):

    if request.method == "GET":
        
        return render(request,"hod/FacultySignUp.html")

    elif request.method == "POST":
        name  = request.POST["name"]
        authority = "faculty"
        email  = request.POST["email"]
        password  = request.POST["password"]
        phone = request.POST["phone"]
        address  = request.POST["address"]
        qualification  = request.POST["qualification"]

        objRegis = Register(name=name,authority=authority,email=email,password=password,phone=phone,address=address)
        objFaculty = Faculty(regis = objRegis,qualification=qualification)

        try:
            objRegis.save()
            objFaculty.save()

            return render(request,"hod/FacultySignUp.html",{"message":"Data saved successfully","class":"alert alert-success"})
        except:
            return render(request,"hod/FacultySignUp.html",{"message":"Some Error Occured","class":"alert alert-danger"})

def queries(request):
    if request.method == "GET":
        queryData = Query.objects.all()
        return render(request,"hod/queries.html",{"data":queryData})

def noticeView(request):
    if request.method == "GET":
        
        return render(request,"hod/notice_view.html")

def classroom_student(request,name):
    info = get_object_or_404(Register,name=name)

    for da in Student.objects.all():
        if(da.regis.name == info.name):
            sinfo = da

    dat = Questions.objects.filter(Class=sinfo.Class,section=sinfo.section)
    faculty_data = Allotment.objects.filter(Class=sinfo.Class,section=sinfo.section)
    student_data = Student.objects.filter(Class=sinfo.Class,section=sinfo.section)

    if request.method == "GET":
        return render(request,"student/classroom_student.html",{"information":sinfo,"data":dat,"receiver_faculty":faculty_data,"receiver_student":student_data})

    elif request.method == "POST":
        pass

def make_submission(request,pk,name):

    info = get_object_or_404(Register,name=name)
    qobj = get_object_or_404(Questions,pk=pk)

    if request.method == "GET":
        return render(request,"student/make_submission.html",{"information":info,"question":qobj})

    elif request.method == "POST":
        
        question = request.POST["question"] 
        faculty = request.POST["faculty_name"]
        student = request.POST["name"]
        Class = request.POST["class"]
        section = request.POST["section"]
        file = request.FILES["File"]

        aobj = Answers(question=question,faculty=faculty,student=student,Class=Class,file=file,section=section,status="submitted")

        try:
            aobj.save()
            return render(request,"student/make_submission.html",{"information":info,"question":qobj,"message":"Assignment Submitted successfully !!","class":"alert alert-success"})
        except:
            return render(request,"student/make_submission.html",{"information":info,"question":qobj,"message":"Try again !!","class":"alert alert-danger"})

def classroom_student_home(request,name):
    info = get_object_or_404(Register,name=name)

    for da in Student.objects.all():
        if(da.regis.name == info.name):
            sinfo = da

    fdata = Allotment.objects.filter(Class=sinfo.Class,section=sinfo.section)
    noticedata = Notice.objects.filter(Class=sinfo.Class,section=sinfo.section)

    if request.method == "GET":
    
        return render(request,"student/student_home_contd.html",{"information":info,"student_info":sinfo,"notice":noticedata,"faculty":fdata})

    elif request.method == "POST":
        
        name = request.POST["name"]
        faculty = request.POST["faculty"]
        Class = request.POST["class"]
        section = request.POST["section"]
        query = request.POST["query"]

        qobj = Query(name=name,faculty=faculty,query=query,Class=Class,section=section)

        try:
            qobj.save()
            return render(request,"student/student_home_contd.html",{"information":info,"notice":noticedata,"faculty":fdata,"message":"Query Successfully Saved !!","class":"alert alert-success"})
        except:
            return render(request,"student/student_home_contd.html",{"information":info,"notice":noticedata,"faculty":fdata,"message":"Error Occured .. Try Again !!","class":"alert alert-danger"})

def assignTask(request,name):
    info = get_object_or_404(Register,name=name)
    if request.method == "GET":
        return render(request,"faculty/viewSubmission.html",{"information":info})

def fees(request,name):
    sdata = get_object_or_404(Register,name=name)
    for da in Student.objects.all():
        if(da.regis.name == sdata.name):
            data = da
    if request.method == "GET":
        return render(request,"student/fees.html",{"data":data})

def library(request,name):
    if request.method == "GET":
        return render(request,"student/Library.html")


def aboutUs(request):
    if request.method == "GET":
        return render(request,"about_us.html")

def queryFetch(request,name):

    if request.method == "GET":
        qdata = Query.objects.filter(faculty=name)
        serial = QuerySerializer(qdata,many=True)

        return JsonResponse(serial.data,safe=False)


@csrf_exempt
def queryDelete(request,pk):
    try:
        data = Query.objects.get(pk=pk)
    except data.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "DELETE":
        data.delete()

        return HttpResponse(status=204)


@csrf_exempt
def noticeget(request):
    noticeData = Notice.objects.all()
    if request.method == "GET":
        serial = NoticeSerializer(noticeData,many=True)
        return JsonResponse(serial.data,safe=False)

@csrf_exempt
def noticeDelete(request,pk):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

@csrf_exempt
def messageGet(request):

    messageData = Message.objects.all()

    if request.method == "GET":

        serial = MessageSerializer(messageData,many=True)
        return JsonResponse(serial.data,safe=False)

@csrf_exempt
def messagePost(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serial = MessageSerializer(data=data)

        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data,status=201)
        return JsonResponse(serial.errors,status=400)

@csrf_exempt
def linkpost(request,name):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serial = LinkSerializer(data=data)

        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data,status=201)
        return JsonResponse(serial.errors,status=400)

@csrf_exempt
def viewSubmission(request,name):
    if request.method == "GET":
        data = Answers.objects.filter(faculty=name)
        serial = AnswersSerializer(data,many=True)
        return JsonResponse(serial.data,safe=False)
    elif request.method == "POST":
        pass

def linkView(request,name):
    sdata = get_object_or_404(Register,name=name)
    data = get_object_or_404(Student,regis=sdata.id)

    linknotice = Link.objects.filter(Class=data.Class,section=data.section)

    linkserial = LinkSerializer(linknotice,many=True)

    return JsonResponse(linkserial.data,safe=False)