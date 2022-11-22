from django.db import models
from base.models import *
from .validators import *


class StudentModel(BaseUser):
    resume = models.FileField(upload_to="resume", max_length=100, blank=True, validators=[validate_file_extension_pdf, validate_file_size])
    headshot = models.ImageField(upload_to="headshot", height_field=None, width_field=None, max_length=None, blank=True)
    linkedIn_link = models.URLField(max_length=200, null=True, blank=True)
    gitHub_link = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.f_name
    class Meta:
        db_table = 'student'


class TeacherModel(BaseUser):
    def __str__(self):
        return self.f_name
    class Meta:
        db_table = 'teacher'
