from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterView

app_name = "user"

urlpatterns = [
    # Url that directs to the register view
    path('register/', RegisterView.as_view(), name='auth_register'),
    ]
