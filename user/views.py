from datetime import datetime

import jwt
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
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

from .models import Customer, CustomerLogin, Department, Employee, EmployeeLogin

from .serializer import RegisterSerializer, CustomerSerializer, DepartmentSerializer, RegisterEmployeeSerializer


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


@api_view(['POST'])
# login view
def login(request, username):
    cust = Customer.objects.get(customer_email=username)
    if cust is not None:
        refresh = RefreshToken.for_user(cust)
        token = str(refresh.access_token)
        login = CustomerLogin(customer=cust,
                              login_token=token,
                              date=datetime.today())
        login.save()
        print("authenticated and token sent")
        return JsonResponse({'token': token}, status=200)
        # logged in
    else:
        return JsonResponse({'error': "no associated account"}, status=400)


@api_view(['POST'])
def elogin(request, username):
    emp = Employee.objects.get(employee_email=username)
    if emp is not None:
        refresh = RefreshToken.for_user(emp)
        token = str(refresh.access_token)
        login = EmployeeLogin(employee=emp,
                              login_token=token,
                              date=datetime.today())
        admin_status = emp.is_admin
        login.save()
        return JsonResponse({'token': token,
                             'admin_status': admin_status}, status=200)

    else:
        return JsonResponse({'error': "no employee account"}, status=400)


@api_view(['GET'])
def getDepartments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)

    return Response(data=serializer.data)
