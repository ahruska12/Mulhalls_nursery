from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PlantSerializer
from .models import Plant


# Create your views here.

@api_view(['GET'])
def get_plant_list(self):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    print("all plants found and sent for getPlantList API call")
    return Response(data=serializer.data)
