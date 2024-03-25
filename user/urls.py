from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from .views import RegisterView, login, get_customer_account, RegisterEmpView, getDepartments, elogin

app_name = "user"

urlpatterns = [
    # Url that directs to the register view
    path('register/customer', RegisterView.as_view(), name='auth_register'),
    path('register/employee', RegisterEmpView.as_view(), name='emp_register'),
    path('auth/<str:username>', login),
    path('auth/employee/<str:username>', elogin),
    path('find-account/customer/<str:email>', get_customer_account),
    path('departments', getDepartments)
]
