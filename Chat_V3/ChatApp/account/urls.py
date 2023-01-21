
from django import views
from django.urls import path
from .import views 
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/',
         LoginView.as_view(template_name='account/login.html'),
         name='login'),
    path('profile/logout/',
         LogoutView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('signup/',views.register,name='signup'),
    


]