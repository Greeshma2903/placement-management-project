from django.db import models
from base.models import *
from .validators import *


class SkillsModel(BaseModel):
    skill_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'skills'
    def __str__(self):
        return self.skill_name


class TeacherModel(MyBaseUser):
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'teacher'


class StudentModel(MyBaseUser):
    resume = models.FileField(upload_to="resume", max_length=100, blank=True, validators=[validate_file_extension_pdf, validate_file_size])
    headshot = models.ImageField(upload_to="headshot", height_field=None, width_field=None, max_length=None, blank=True)
    linkedIn_link = models.URLField(max_length=200, null=True, blank=True)
    gitHub_link = models.URLField(max_length=200, null=True, blank=True)
    job = models.TextField()
    department = models.TextField()
    bio = models.TextField(null=True, blank=True)
    # skills = models.ManyToManyField(SkillsModel, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    def __str__(self):
             return self.name 
    class Meta:
        db_table = 'student'
