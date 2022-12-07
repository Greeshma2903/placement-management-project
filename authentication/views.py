from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import logout , login
from .models import *
from django.contrib import messages
  
def loginUser(request):
    return render(request, 'base.html')
 
def doLogin(request):
     
    print("here")
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    user_type = request.GET.get('user_type')

    print(email_id)
    print(password)
    print(request.user)
    if not (email_id and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'tpo-base.html')
 
    user = CustomUser.objects.filter(email=email_id, password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'base.html')
    
    print(email_id)
    print(password)
    print(request.user)
    if not (email_id and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'student-base.html')
 
    user = CustomUser.objects.filter(email=email_id, password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'base.html')

    login(request, user)
    print(request.user)
 
    if user.user_type == CustomUser.student:
             return redirect('student-base/')
    elif user.user_type == CustomUser.teacher:
        return redirect('tpo-base/')
 
    return render(request, 'student-base.html')
 
     
def registration(request):
    return render(request, 'base.html')
     
 
def doRegistration(request):
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    confirm_password = request.GET.get('confirmPassword')
 
    print(email_id)
    print(password)
    print(confirm_password)
    if not (email_id and password and confirm_password):
        messages.error(request, 'Please provide all the details!!')
        return render(request, 'tpo-base.html')
     
    if password != confirm_password:
        messages.error(request, 'Both passwords should match!!')
        return render(request, 'tpo-base.html')
 
    is_user_exists = CustomUser.objects.filter(email=email_id).exists()
 
    if is_user_exists & user_type == CustomUser.teacher:
        messages.error(request, 'User with this email id already exists. Please proceed to login!!')
        return render(request, 'tpo-base.html')
    elif user_type == CustomUser.student:
        return render(request, 'student-base.html')
 
    user_type = get_user_type_from_email(email_id)
 
    if user_type is None:
        return messages.error(request, "Please use valid format for the email id: ")

    if user_type == CustomUser.teacher:
        return render(request, 'tpo-base.html')
    elif user_type == CustomUser.student:
        return render(request, 'student-base.html')
 
    email = email_id.split('@')[0].split('.')[0]
 
    if CustomUser.objects.filter(email=email).exists():
        messages.error(request, 'User with this email already exists. Please use different email')
        return render(request, 'tpo-base.html')
    elif CustomUser=='1':
        return render(request, 'student-base.html')

    user = CustomUser()
    user.email = email_id
    user.password = password
    user.user_type = user_type
    user.save()
     
    if user_type == CustomUser.student:
        StudentModel.objects.create(admin=user)
        return render(request, 'student-base.html')
    elif user_type == CustomUser.teacher:
        TeacherModel.objects.create(admin=user)
        return render(request, 'tpo-base.html')
     
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
 
 
def get_user_type_from_email(email_id):
    try:
        email_id = email_id.split('@')[0]
        email_user_type = email_id.split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except:
        return None