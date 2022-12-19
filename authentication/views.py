from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
# from .threads import *
from .models import *
from django.conf import settings

def LogIn_student(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        student_obj = StudentModel.objects.filter(email=email).first()
        if student_obj is None:
            messages.info(request, 'User does not exists. Please Signup')
            return redirect('student-login')
        if not student_obj.is_verified:
            messages.info(request, 'This profile is not verified. Please Check your mail.')
            return redirect('student-login')    
        user = authenticate(email=email, password=password)
        if user is  None:
            messages.info(request, 'Incorrect Password.')
            return redirect('student-login')
        login(request, user)
        messages.success(request, 'Successfully logged in')
        return redirect('student-dashboard')

def LogIn_tpo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        teacher_obj = TeacherModel.objects.filter(email=email).first()
        if teacher_obj is None:
            messages.info(request, 'User does not exists. Please Signup')
            return redirect('tpo-login')
        if not teacher_obj.is_verified:
            messages.info(request, 'This profile is not verified. Please Check your mail.')
            return redirect('tpo-login')    
        user = authenticate(email=email, password=password)
        if user is  None:
            messages.info(request, 'Incorrect Password.')
            return redirect('tpo-login')
        login(request, user)
        messages.success(request, 'Successfully logged in')
        return redirect('tpo-dashboard')
