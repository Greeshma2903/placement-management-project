from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *


# home page
def home_page(request):
    return render(request, "main/home.html")


# all companies page
def all_companies(request):
    return render(request, "main/all-companies.html")


# about page
def about_page(request):
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
                return redirect('student-login')
            login(request, user)
            messages.success(request, 'Successfully logged in')
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
                messages.info(request, 'User does not exists. Please Signup')
                return redirect('tpo-login')
            user = authenticate(email=email, password=password)
            if user is  None:
                messages.info(request, 'Incorrect Password.')
                return redirect('tpo-login')
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('tpo-dashboard')
    except Exception as e:
        print(e)
    return render(request, "accounts/tpo-login.html")


def student_profile(request):
    try:
        pass
    except Exception as e:
        print(e)
