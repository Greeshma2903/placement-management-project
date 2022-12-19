from django.db import models
from base.models import *

class TeacherModel(models.Model):
    id = models.AutoField(primary_key=True)
    # admin = models.OneToOneField( on_delete = models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.uname
    class Meta:
        db_table = 'teacher'

class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # admin = models.OneToOneField( on_delete = models.CASCADE)
    # resume = models.FileField(upload_to="resume", max_length=100, blank=True, validators=[validate_file_extension_pdf, validate_file_size])
    headshot = models.ImageField(upload_to="headshot", height_field=None, width_field=None, max_length=None, blank=True)
    linkedIn_link = models.URLField(max_length=200, null=True, blank=True)
    gitHub_link = models.URLField(max_length=200, null=True, blank=True)
    skills = models.TextField()
    job = models.TextField()
    objects = models.Manager()
    department = models.TextField()
    def __str__(self):
             return self.uname 
    class Meta:
        db_table = 'student'
