from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterView, customer_obtain_jwt_token, get_customer_account

app_name = "user"

urlpatterns = [
    # Url that directs to the register view
    path('register/customer', RegisterView.as_view(), name='auth_register'),
    path('auth/', customer_obtain_jwt_token),
    path('find-account/customer/<str:email>', get_customer_account),
    ]
