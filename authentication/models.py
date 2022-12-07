from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from base.models import *
from .validators import *

class CustomUser(AbstractUser):
    teacher = '1'
    student = '2'
    
     
    UNAME_TO_USER_TYPE_MAP = {
        'teacher': teacher,
        'student': student
    }
 
    user_type_data = ((teacher, "TeacherModel"), (student, "StudentModel"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
 

class TeacherModel(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return self.uname
    class Meta:
        db_table = 'teacher'

class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resume = models.FileField(upload_to="resume", max_length=100, blank=True, validators=[validate_file_extension_pdf, validate_file_size])
    headshot = models.ImageField(upload_to="headshot", height_field=None, width_field=None, max_length=None, blank=True)
    linkedIn_link = models.URLField(max_length=200, null=True, blank=True)
    gitHub_link = models.URLField(max_length=200, null=True, blank=True)
    objects = models.Manager()
    def __str__(self):
             return self.uname 
    class Meta:
        db_table = 'student'
