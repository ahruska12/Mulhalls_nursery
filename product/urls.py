from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from .views import get_plant_list, getPlantByType, getPlantByDept, getPlantByColor, getPlantByTypeCategory, \
    getPlantByID, getPopularSearches, getPlantPrev, getPlantsByArr

app_name = "product"

urlpatterns = [
    path('home/', get_plant_list, name='plant-list'),
    path('plant/prev/<int:plant_id>', getPlantPrev, name='plant-prev'),
    path('plant/select/<int:plant_id>', getPlantByID, name='plant-id'),
    path('plant/type/<str:plant_type>', getPlantByType, name='plant-type'),
    path('plant/category/<str:plant_type>/<str:category>', getPlantByTypeCategory, name='plant-special-type'),
    path('plant/dept/<int:dept>', getPlantByDept, name='plant-dept'),
    path('plant/color/<str:color>', getPlantByColor, name='plant-color'),
    path('plant/group', getPlantsByArr, name='plant-type'),

    path('popular/', getPopularSearches, name='popular-plants'),
]
