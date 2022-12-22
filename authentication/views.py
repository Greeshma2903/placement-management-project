from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .threads import *
from .models import *
from .utils import *
import xlrd

context = {}

# home page
def home_page(request):
    return render(request, "main/home.html")

# about page
def about_page(request):
    messages.info(request, 'User does not exists. Please Signup')
    return render(request, "main/about.html")


# student login
def student_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            student_obj = StudentModel.objects.filter(email=email).first()
            if student_obj is None:
                messages.info(request, 'User does not exists. Please Signup')
                return redirect('student-login')
            user = authenticate(email=email, password=password)
            if user is  None:
                messages.info(request, 'Incorrect Password.')
                return redirect('student-login/')
            login(request, user)
            messages.success(request, 'Student Successfully logged in')
            return redirect('student-dashboard')
    except Exception as e:
        print(e)
    return render(request, "accounts/student-login.html")

    
# tpo login
def tpo_login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            teacher_obj = TeacherModel.objects.filter(email=email).first()
            if teacher_obj is None:
                messages.info(request, 'User does not exists.')
                return redirect('signup')  
            user = authenticate(email=email, password=password)
            if user is  None:
                messages.info(request, 'Incorrect Password.')
                return redirect('login')
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('tpo-dashboard')
    except Exception as e:
        print(e)
    return render(request, "accounts/tpo-login.html")


# student profile
@login_required(login_url='/student-login/')
def student_profile(request):
    context["user"] = StudentModel.objects.get(email=request.user)
    return render(request, "student/profile.html", context)


# student profile
@login_required(login_url='/student-login/')
def update_student_profile(request):
    try:
        user = StudentModel.objects.get(email=request.user)
        if request.method == 'POST':
            user.resume = request.FILES['resume']
            user.headshot = request.POST.get("headshot")
            user.linkedIn_link = request.POST.get("linkedIn_link")
            user.gitHub_link = request.POST.get("gitHub_link")
            user.bio = request.POST.get("bio")
            user.skills = request.POST.get("skills")
            user.save()
            print("@@@@@@@@@")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except Exception as e:
        print(e)
    return render(request, "student/profile.html", context)


# add students data
@login_required(login_url='/tpo-login/')
def add_student_data(request):
    try:
        if request.method == 'POST':
            file_obj = FileSavingModel.objects.create(file=request.FILES['file'])
            path = str(file_obj.file.path)
            workbook = xlrd.open_workbook(path)
            sheet = workbook.sheet_by_index(0)
            for row in range(1,sheet.nrows):
                org = StudentModel.objects.create(
                    name = str(sheet.cell_value(row,0)),
                    email = str(sheet.cell_value(row,1)).lower(),
                    phone = sheet.cell_value(row,2)
                )
                pw = get_random_string(8)
                org.set_password(pw)
                thread_obj = send_credentials_mail(str(sheet.cell_value(row,1)).lower(), pw)
                thread_obj.start()
                org.save()
    except Exception as e:
        print(e)
    return render(request, "tpo/add-students.html")


# student logout
@login_required(login_url='/student-login/')
def student_logout(request):
    logout(request)
    messages.info(request, 'Logged Out')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# tpo logout
@login_required(login_url='/tpo-login/')
def tpo_logout(request):
    logout(request)
    messages.info(request, 'Logged Out')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# add tpo
def create_tpo(request):
    obj = TeacherModel.objects.create(name="Manisha", email="manisha@gmail.com")
    obj.set_password("password")
    obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
