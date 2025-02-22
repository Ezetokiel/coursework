from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('home/', views.homePage, name='home')
]