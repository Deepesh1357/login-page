from django.contrib import admin
from django.urls import path
from hallo import views


urlpatterns = [
    path("",views.login, name='login'),
    path("login",views.login, name='login'),
    path("SignUp",views.SighUp, name='SignUp'),
    path("welcome",views.welcome, name='welcome')
]
