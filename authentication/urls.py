from django.urls import path
from . import views
from .views import *

urlpatterns = [
	 path("login-student/", views.LogIn_student, name="student-login"),
	 path("login-top/", views.LogIn_tpo, name="tpo-login"),
]