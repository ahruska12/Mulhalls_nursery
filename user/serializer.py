from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     style={'input_type': 'password'},
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True,
                                      style={'input_type': 'password'},
                                      required=True)

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  'password2',
                  'email',
                  'first_name',
                  'last_name',
                  'is_staff',
                  'is_superuser'
                  )
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True},
                        'password': {'write_only': True, 'min_length': 6},
                        'password2': {'write_only': True, 'min_length': 6}
                        }

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})
            return attrs

    def create(self, validated_data):
        is_staff = validated_data.pop('is_staff', False)
        is_superuser = validated_data.pop('is_superuser', False)

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user