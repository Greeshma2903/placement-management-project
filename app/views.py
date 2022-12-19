from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from authentication.models import *
from .models import *

context = {}


# all companies page
def all_companies(request):
    context["companies"] = CompanyModel.objects.all()
    # context["companies"] = CompanyModel.objects.raw('SELECT * FROM myapp_person')
    return render(request, "main/all-companies.html", context)


# job list
@login_required(login_url='/student-login/')
def listed_jobs(request):
    context["jobs"] = JobModel.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "main/all-companies.html", context)


# student dashboard
@login_required(login_url='/student-login/')
def student_dashboard(request):
    try:
        user = StudentModel.objects.get(email=request.user)
        objs = JobApplication.objects.filter(applicant=user)
        context["profile"] = user
        context["applications"] = objs
    except Exception as e:
        print(e)
    return render(request, "dashboard/stu-dash.html", context)


# tpo dashboard
@login_required(login_url='/tpo-login/')
def tpo_dashboard(request):
    try:
        context["applications"] = JobApplication.objects.all()
    except Exception as e:
        print(e)
    return render(request, "dashboard/tpo-dash.html", context)
