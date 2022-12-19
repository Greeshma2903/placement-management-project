from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path("all-companies/", views.all_companies, name='all-companies'),

	path("student-dashboard/", views.student_dashboard, name='student-dashboard'),
	path("tpo-dashboard/", views.tpo_dashboard, name='tpo-dashboard'),
	
	path("tpo/job-applicants/<job_id>/", views.tpo_applicants_list, name='job-applicants'),
	
	path("tpo/accept/<application_id>/", views.tpo_accept_application, name='job-applicants-accept'),
	path("tpo/reject/<application_id>/", views.tpo_reject_application, name='job-applicants-reject'),
	
	path("all-companies/", views.all_companies, name='all-companies'),
]