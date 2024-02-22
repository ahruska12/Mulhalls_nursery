from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import User
from .models import Customer
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    customer_email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )
    customer_password = serializers.CharField(write_only=True,
                                              required=True,
                                              style={'input_type': 'password'},
                                              validators=[validate_password])
    password2 = serializers.CharField(write_only=True,
                                      style={'input_type': 'password'},
                                      required=True)

    class Meta:
        model = Customer
        fields = ('customer_email',
                  'customer_password',
                  'customer_first_name',
                  'customer_last_name',
                  'password2'
                  )
        extra_kwargs = {
            'password2': {'write_only': True, 'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['customer_password'] != attrs['password2']:
            raise serializers.ValidationError({"customer_password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data['customer_password'] = make_password(validated_data['customer_password'])
        print(validated_data)
        user = Customer.objects.create(
            customer_email=validated_data['customer_email'],
            customer_first_name=validated_data['customer_first_name'],
            customer_last_name=validated_data['customer_last_name'],
            customer_password=validated_data['customer_password']
        )
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class meta:
        model = Customer
        fields = ['__all__']
