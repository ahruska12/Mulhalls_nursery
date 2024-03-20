from datetime import datetime

from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import jwt
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializer import PlantSerializer
from .models import Plant


# Create your views here.
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


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_plant_list(request):
    result = authenticate(request)
    if result is not None:
        print("request", request.user)
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    else:
        return JsonResponse({"Error": "Error authenticating"}, status=401)