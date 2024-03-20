from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Plant, Annual, Perennial, Shrub, Tree


class PerennialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perennial
        fields = "__all__"


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = "__all__"


class ShrubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shrub
        fields = "__all__"


class AnnualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annual
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"
