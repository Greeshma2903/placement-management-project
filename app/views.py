from django.shortcuts import render
from app.models import CompanyModel , JobModel , JobApplication

def login(request):
     return render(request,'base.html')
# Create your views here.
