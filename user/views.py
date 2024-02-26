from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import User
from rest_framework_jwt.settings import api_settings

from .models import Customer

from .serializer import RegisterSerializer, CustomerSerializer


# generic view for registering to our site

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@api_view(['GET'])
def get_customer_account(self, email):
    customer = Customer.objects.get(customer_email=email)
    serializer = CustomerSerializer(customer)
    print(customer, "customer found and sent")
    return Response(data=serializer.data)

@api_view(['POST'])
def customer_obtain_jwt_token(request):
    if request.method == 'POST':
        email = request.data.get('username')
        password = request.data.get('password')
        print(email, password)
        try:
            cust = Customer.objects.get(customer_email=email, customer_password=password)
            print("customer found")
        except Customer.DoesNotExist:
            print("customer not found")
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
        if cust is not None:
            print("user authenticated")
            # get token
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(cust)
            token = jwt_encode_handler(payload)
            return JsonResponse({'token': token}, status=200)
        print("user not authenticated")
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
