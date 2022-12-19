from django.contrib import admin
from .models import *


class JobModelAdmin(admin.ModelAdmin):
    list_display = ["position", "company", "pay_rate", "is_active"]    
admin.site.register(JobModel,JobModelAdmin)

admin.site.register(CompanyModel)
admin.site.register(JobApplicationModel)
