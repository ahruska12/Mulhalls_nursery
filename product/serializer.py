from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Plant, Annual, Perennial, Shrub, Tree
from user.models import Department


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


class PlantPrevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "plant_name", "plant_picture"


class CreatePlantSerializer(serializers.ModelSerializer):
    plant_type = serializers.CharField(required=True)
    plant_name = serializers.CharField(required=True)
    plant_size = serializers.CharField(required=True)
    plant_color = serializers.CharField(required=True)
    plant_description = serializers.CharField(required=True)
    plant_picture = serializers.ImageField(required=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Plant
        fields = ["plant_id",
                  "plant_type",
                  "plant_name",
                  "plant_size",
                  "plant_color",
                  "plant_description",
                  "plant_picture",
                  "department_id", ]

    def create(self, validated_data):
        plant = Plant.objects.create(

        )
