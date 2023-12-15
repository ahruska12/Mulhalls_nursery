from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from user import views

app_name = "user"

urlpatterns = [
    # Url that directs to the register view
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    ]
