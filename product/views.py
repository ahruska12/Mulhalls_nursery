from datetime import datetime

from django.db.models import Count
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.authtoken.models import Token
import jwt
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import PlantSerializer, PlantPrevSerializer, CreatePlantSerializer, CreateAnnualSerializer, \
    CreatePerennialSerializer, CreateTreeSerializer, CreateShrubSerializer

from .models import Plant, Tree, Shrub, Annual, Perennial

# Create your views here.
"""
def authenticate(request):
    try:
        for token in Token.objects.all():
            print(request.auth)
            if request.auth == token.key:
                return token.user_id
    except Token.DoesNotExist:
        return None


def is_valid_token(token):
    try:
        # Decode the token without verifying the signature
        payload = jwt.decode(token, options={"verify_signature": False})  # Adjusted for jwt.decode API

        # Check if the 'exp' claim is present and not expired
        if 'exp' in payload:
            expiration_timestamp = payload['exp']
            current_timestamp = datetime.utcnow().timestamp()
            if expiration_timestamp >= current_timestamp:
                print("token not expired")
                return True
            else:
                print("Token has expired")
                return False
        else:
            print("Token does not contain expiration claim")
            return False
    except jwt.DecodeError:
        print("Invalid token")
        return False
"""


@api_view(['GET'])
def get_plant_list(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantByType(request, plant_type):
    print(f"collecting all {plant_type} plants")
    plants = Plant.objects.filter(plant_type=plant_type.capitalize())
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantByDept(request, dept):
    print(f"collecting all department {dept} plants")
    plants = Plant.objects.filter(department_id=dept)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantByColor(request, color):
    print(f"collecting all department {color} plants")
    plants = Plant.objects.filter(plant_color=color.capitalize())
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantByTypeCategory(request, plant_type, category):
    result = []
    category.capitalize()
    plant_type.capitalize()
    print(f"all plants matching {plant_type} type and {category} category")
    if plant_type.capitalize() == "Tree":
        print("tree type")
        plants = Tree.objects.filter(tree_category=category.capitalize())
        for plant in plants:
            plants = Plant.objects.get(plant_id=plant.plant_id)
            result.append(plants)

    elif plant_type.capitalize() == "Shrub":
        print("shrub type")
        plants = Shrub.objects.filter(shrub_category=category.capitalize())
        for plant in plants:
            plants = Plant.objects.get(plant_id=plant.plant_id)
            result.append(plants)

    elif plant_type.capitalize() == "Perennial":
        print("perennial type")
        plants = Perennial.objects.filter(perennial_category=category.capitalize())
        for plant in plants:
            plants = Plant.objects.get(plant_id=plant.plant_id)
            result.append(plants)

    elif plant_type.capitalize() == "Annual":
        print("shrub type")
        plants = Annual.objects.filter(annual_category=category.capitalize())
        for plant in plants:
            plants = Plant.objects.get(plant_id=plant.plant_id)
            result.append(plants)

    serializer = PlantSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantByID(request, plant_id):
    print(f"collecting all {plant_id} plants")
    plant = Plant.objects.get(plant_id=plant_id)
    serializer = PlantSerializer(plant)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantPrev(request, plant_id):
    plant = Plant.objects.get(plant_id=plant_id)
    serializer = PlantPrevSerializer(plant)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantsByArr(request):
    # Get plant ids from request query parameters
    ids = request.query_params.get('ids')
    if ids:
        # Convert ids from comma-separated string to a list of integers
        ids_list = [int(id) for id in ids.split(',')]
        # Query the database for plants with these IDs
        plants = Plant.objects.filter(plant_id__in=ids_list)
        # Serialize the queryset
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)


class addPlant(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            plant = serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class addAnnual(generics.CreateAPIView):
    serializer_class = CreateAnnualSerializer


class addPerennial(generics.CreateAPIView):
    serializer_class = CreatePerennialSerializer


class addTree(generics.CreateAPIView):
    serializer_class = CreateTreeSerializer


class addShrub(generics.CreateAPIView):
    serializer_class = CreateShrubSerializer
