from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path("all-companies", views.all_companies, name='all-companies'),
]