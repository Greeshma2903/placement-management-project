from django.urls import path
from . import views
from .views import *

urlpatterns = [

	path("", views.home_page, name='home-page'),
	path("about/", views.about_page, name='about'),

	path("student-login/", views.student_login, name="student-login"),
	path("tpo-login/", views.tpo_login, name="tpo-login"),

	path("student-logout/", views.student_logout, name="student-logout"),
	path("tpo-logout/", views.tpo_logout, name="tpo-logout"),
	
	path("tpo-create/", views.create_tpo, name="tpo-create"),

	path("student-profile/", views.student_profile, name="student-profile"),
	path("update-student-profile/", views.update_student_profile, name="update-student-profile"),

	path("tpo/add-students-details/", views.add_student_data, name="add-student-details"),

]