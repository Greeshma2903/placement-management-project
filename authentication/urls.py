from django.urls import path
from . import views
from .views import *

urlpatterns = [
	 #path('signup/', views.signUp, name="signup"),
	 path('base/', views.loginUser, name="login"),
	 path('base/', views.logout_user, name="logout"),
	# path('forgot/', views.forgot, name="forgot"),
	# path('reset/', views.reset, name="reset"),
]