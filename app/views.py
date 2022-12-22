from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from authentication.models import *
from .threads import *
from .models import *

context = {}


# all companies page
def all_companies(request):
    context["companies"] = CompanyModel.objects.all()
    # context["companies"] = CompanyModel.objects.raw('SELECT * FROM company')
    return render(request, "main/all-companies.html", context)


# job single
@login_required(login_url='/student-login/')
def single_job(request, job_id):
    context["job"] = JobModel.objects.get(id=job_id)
    # context["job"] = JobModel.objects.raw(f"SELECT * FROM job where id={job_id}")
    return render(request, "student/job-desc.html", context)


# student dashboard
@login_required(login_url='/student-login/')
def student_dashboard(request):
    try:
        user = StudentModel.objects.get(email=request.user)
        context["jobs"] = JobModel.objects.filter(is_active=True).order_by("-created_at")
        # context["jobs"] = JobModel.objects.raw('SELECT * FROM job where is_active=true created_at dec')
        context["applications"] = JobApplicationModel.objects.filter(applicant=user)
    except Exception as e:
        print(e)
    return render(request, "dashboard/stu-dash.html", context)


# tpo dashboard
@login_required(login_url='/tpo-login/')
def tpo_dashboard(request):
    try:
        context["jobs"] = JobModel.objects.all().order_by("-created_at")
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
    return render(request, "tpo/applicants-list.html", context)


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


# Apply for Job
@login_required(login_url='/student-login/')
def apply_for_job(request, job_id):
    try:
        user = StudentModel.objects.get(email=request.user)
        job =JobModel.objects.get(id=job_id)
        app_obj, _ = JobApplicationModel.objects.get_or_create(job=job, applicant=user, status="Applied")
        thread_obj = send_applied_mail(user.email, job.company.company_name, job.position)
        thread_obj.start()
        app_obj.save()
        return redirect("student-dashboard")
    except Exception as e:
        print(e)
    return render(request, "student/job-desc.html", context)
