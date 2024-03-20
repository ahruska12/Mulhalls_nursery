from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from .views import get_plant_list

app_name = "product"

urlpatterns = [
    path('home/', get_plant_list, name='plant-list'),
]
