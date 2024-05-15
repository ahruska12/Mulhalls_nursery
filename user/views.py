from datetime import datetime

import jwt
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Customer, CustomerLogin, Department, Employee, EmployeeLogin, QuestionsAsked, SearchHistory

from .serializer import RegisterSerializer, CustomerSerializer, DepartmentSerializer, RegisterEmployeeSerializer, \
    EmployeeSerializer, QuestionAskedSerializer, QuestionSerializer, QuestionAnsweredSerializer, CreateSearchSerializer
from product.serializer import PlantSerializer

from product.models import Plant


# generic view for registering to our site

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class RegisterEmpView(generics.CreateAPIView):
    print("register view called")
    serializer_class = RegisterEmployeeSerializer


@api_view(['GET'])
def get_customer_account(self, email):
    customer = Customer.objects.get(customer_email=email)
    serializer = CustomerSerializer(customer)
    print(customer, "customer found and sent")
    return Response(data=serializer.data)


@api_view(['GET'])
def get_employee_account(self, email):
    employee = Employee.objects.get(employee_email=email)
    serializer = EmployeeSerializer(employee)
    print(employee, "employee found and sent")
    return Response(data=serializer.data)


@api_view(['POST'])
# login view
def login(request, username):
    try:
        cust = Customer.objects.get(customer_email=username)
        return JsonResponse({'success': "Account approved"}, status=200)
        # logged in
    except Customer.DoesNotExist:
        return JsonResponse({'error': "no associated account"}, status=400)


@api_view(['POST'])
def elogin(request, username):
    try:
        emp = Employee.objects.get(employee_email=username)
        return JsonResponse({'admin_status': "is admin"}, status=200)
    except Employee.DoesNotExist:
        return JsonResponse({'error': "no employee account"}, status=400)

@api_view(['GET'])
def getDepartments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)

    return Response(data=serializer.data)


class QuestionAsked(generics.CreateAPIView):
    serializer_class = QuestionAskedSerializer


@api_view(['GET'])
def getAllQuestions(request, var=None):
    if var is not None:
        questions = QuestionsAsked.objects.filter(is_answered=False)
    else:
        questions = QuestionsAsked.objects.all()
    serializer = QuestionSerializer(questions, many=True)

    return Response(data=serializer.data)


@api_view(['GET'])
def getQuestionsByCust(request, cust_id):
    questions = QuestionsAsked.objects.filter(customer_id=cust_id)
    serializer = QuestionSerializer(questions, many=True)

    return Response(data=serializer.data)


@api_view(['GET'])
def getQuestionsByPlant(request, plant_id):
    questions = QuestionsAsked.objects.filter(plant_id=plant_id,
                                              is_answered=True)
    serializer = QuestionSerializer(questions, many=True)

    return Response(data=serializer.data)


@api_view(['GET'])
def getQuestionsByID(request, question_id):
    questions = QuestionsAsked.objects.get(question_id=question_id)
    serializer = QuestionSerializer(questions)

    return Response(data=serializer.data)


class AnswerQuestion(generics.CreateAPIView):
    serializer_class = QuestionAnsweredSerializer


@api_view(['GET'])
def getPopularSearches(request):
    plant_search_counts = SearchHistory.objects.values('plant_id').annotate(search_count=Count('plant_id')).order_by(
        '-search_count')[:5]

    plant_ids = [entry['plant_id'] for entry in plant_search_counts]

    top_plants = Plant.objects.filter(plant_id__in=plant_ids).order_by('-plant_id')

    serializer = PlantSerializer(top_plants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPlantByUserSearch(request, user_id):
    recent_searches = []
    plant_ids_seen = set()
    print(f"collecting all plants for {user_id}")
    plants = SearchHistory.objects.filter(customer_id=user_id).order_by('-search_date')
    for plant in plants:
        if plant.plant_id not in plant_ids_seen:
            p = Plant.objects.get(plant_id=plant.plant_id)
            recent_searches.append(p)
            plant_ids_seen.add(plant.plant_id)

        # Stop if we have collected 5 unique plants
        if len(recent_searches) == 5:
            break
    serializer = PlantSerializer(recent_searches, many=True)
    return Response(serializer.data)


class addPlantSearch(generics.CreateAPIView):
    serializer_class = CreateSearchSerializer
