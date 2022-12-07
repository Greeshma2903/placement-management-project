from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('login/', views.loginUser, name="login"),
]