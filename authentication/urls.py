from django.urls import path
from . import views
from .views import *

urlpatterns = [
	 path("base/", views.LogIn_student, name="student-login"),
	 path("base/", views.LogIn_tpo, name="tpo-login"),
]