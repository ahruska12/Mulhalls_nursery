from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Customer, Employee, Department
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    print("register serializer started")
    customer_email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=Customer.objects.all())])
    customer_password = serializers.CharField(write_only=True,
                                              required=True,
                                              style={'input_type': 'password'},
                                              validators=[validate_password]
                                              )
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

    def create(self, validated_data):
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
    class Meta:
        model = Customer
        fields = '__all__'


class RegisterEmployeeSerializer(serializers.ModelSerializer):
    print("serializer called")
    employee_email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=Employee.objects.all())])
    print("email vvalidated")
    employee_password = serializers.CharField(write_only=True,
                                              required=True,
                                              style={'input_type': 'password'},
                                              validators=[validate_password]
                                              )
    password2 = serializers.CharField(write_only=True,
                                      style={'input_type': 'password'},
                                      required=True)

    class Meta:
        model = Employee
        fields = ('employee_email',
                  'employee_password',
                  'employee_first_name',
                  'employee_last_name',
                  'is_admin',
                  'department',
                  'password2'
                  )
        extra_kwargs = {
            'password2': {'write_only': True, 'min_length': 6}
        }

    def create(self, validated_data):
        print(validated_data)
        emp = Employee(
            employee_email=validated_data['employee_email'],
            employee_first_name=validated_data['employee_first_name'],
            employee_last_name=validated_data['employee_last_name'],
            employee_password=validated_data['employee_password'],
            department=validated_data['department'],
            is_admin=validated_data['is_admin']
        )
        emp.save()
        return emp


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
