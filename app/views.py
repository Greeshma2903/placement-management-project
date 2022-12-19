from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authentication.models import *
from .threads import *
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
        context["jobs"] = JobModel.objects.filter(is_active=True)
        context["applications"] = JobApplicationModel.objects.filter(applicant=user)
    except Exception as e:
        print(e)
    return render(request, "dashboard/stu-dash.html", context)


# tpo dashboard
@login_required(login_url='/tpo-login/')
def tpo_dashboard(request):
    try:
        context["jobs"] = JobApplicationModel.objects.filter(job__is_active=True)
    except Exception as e:
        print(e)
    return render(request, "dashboard/tpo-dash.html", context)


# tpo dashboard
@login_required(login_url='/tpo-login/')
def tpo_applicants_list(request, job_id):
    try:
        context["job_applicantion"] = JobApplicationModel.objects.filter(job__id=job_id)
    except Exception as e:
        print(e)
    return render(request, "dashboard/tpo-dash.html", context)


# Job Applicaition Accept
def tpo_accept_application(request, application_id):
    try:
        obj = JobApplicationModel.objects.get(id=application_id)
        obj.status = "Accept"
        thread_obj = send_result(obj.applicant.email, obj.job.position, "accepted")
        thread_obj.start()
        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Job Applicaition Reject
def tpo_reject_application(request, application_id):
    try:
        obj = JobApplicationModel.objects.get(id=application_id)
        obj.status = "Reject"
        thread_obj = send_result(obj.applicant.email, obj.job.position, "rejected")
        thread_obj.start()
        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

