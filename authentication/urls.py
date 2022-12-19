from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path("", views.home_page, name='home-page'),
	path("all-companies", views.all_companies, name='all-companies'),
	path("about", views.about_page, name='about'),

	path("student-login/", views.student_login, name="student-login"),
	path("tpo-login/", views.tpo_login, name="tpo-login"),

]