from datetime import datetime, timedelta
from django.db import models
from base.models import BaseModel
from authentication.models import StudentModel
from django.db.models.signals import pre_save
from django.dispatch import receiver

PLACEMENT_STATUS = (("Applied","Applied"),("Placed","Placed"), ("Rejected","Rejected"))


class CompanyModel(BaseModel):
    company_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logo", height_field=None, width_field=None, max_length=None)
    address = models.TextField()
    desc = models.TextField(null=True, blank=True)
    web_link = models.URLField(max_length=200)
    def __str__(self):
        return self.company_name
    class Meta:
        db_table = "company"


class JobModel(BaseModel):
    position = models.CharField(max_length=50)
    company = models.ForeignKey(CompanyModel, related_name="company_job_listing", on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    last_apply_date = models.DateField(auto_now=False, auto_now_add=False)
    pay_rate = models.PositiveIntegerField()
    max_applicant = models.PositiveSmallIntegerField(null=True, blank=True)
    no_of_applicants = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.position
    class Meta:
        db_table = "job"


class JobApplicationModel(BaseModel):
    job = models.ForeignKey(JobModel, related_name="job_applied", on_delete=models.CASCADE)
    applicant = models.ForeignKey(StudentModel, related_name="job_applicant", on_delete=models.CASCADE)
    status = models.CharField(choices=PLACEMENT_STATUS, max_length=10, default=PLACEMENT_STATUS[0])
    def __str__(self):
        return self.applicant.name
    class Meta:
        db_table = "job_application"


@receiver(pre_save, sender=JobApplicationModel)
def update_job_applicants_number(sender, instance, *args, **kwargs):
    try:
        tomorrow = datetime.today() + timedelta(1)
        job_obj = instance.job
        if (job_obj.max_applicant == job_obj.no_of_applicants) or (job_obj.last_apply_date == tomorrow):
            job_obj.is_active = False
            job_obj.save()
        else:   
            job_obj.no_of_applicants += 1
            job_obj.save()
    except Exception as e:
        print(e)
