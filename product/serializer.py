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
    department_id = serializers.CharField(required=True)
    plant_color = serializers.CharField(required=True)
    plant_description = serializers.CharField(required=True)
    plant_name = serializers.CharField(required=True)
    plant_picture = serializers.ImageField(required=False)
    plant_size = serializers.CharField(required=True)
    plant_type = serializers.CharField(required=True)

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
        if validated_data['plant_picture'] != "":
            pic = validated_data['plant_picture']
        else:
            pic = None
        plant = Plant.objects.create(
            plant_type=validated_data['plant_type'],
            plant_name=validated_data['plant_name'],
            plant_size=validated_data['plant_size'],
            plant_color=validated_data['plant_color'],
            plant_description=validated_data['plant_description'],
            plant_picture=validated_data['plant_picture'],
            department_id=validated_data['department_id']
        )
        return plant


class CreateAnnualSerializer(serializers.ModelSerializer):
    plant = serializers.CharField(required=True)
    is_hardy = serializers.BooleanField(required=True)
    is_semi_hardy = serializers.BooleanField(required=True)
    shade_tolerant = serializers.BooleanField(required=True)
    heat_tolerant = serializers.BooleanField(required=True)
    drought_tolerant = serializers.BooleanField(required=True)
    annual_category = serializers.BooleanField(required=True)

    class Meta:
        model = Annual
        fields = ["plant",
                  "is_hardy",
                  "is_semi_hardy",
                  "shade_tolerant",
                  "heat_tolerant",
                  "drought_tolerant",
                  "annual_category"]

    def create(self, validated_data):
        plant = Annual.objects.create(
            plant_type=validated_data['plant_type'],
            plant_name=validated_data['plant_name'],
            plant_size=validated_data['plant_size'],
            plant_color=validated_data['plant_color'],
            plant_description=validated_data['plant_description'],
            plant_picture=validated_data['plant_picture'],
            department_id=validated_data['department_id']
        )
        return plant


class CreatePerennialSerializer(serializers.ModelSerializer):
    department_id = serializers.CharField(required=True)
    plant_color = serializers.CharField(required=True)
    plant_description = serializers.CharField(required=True)
    plant_name = serializers.CharField(required=True)
    plant_picture = serializers.ImageField(required=False)
    plant_size = serializers.CharField(required=True)
    plant_type = serializers.CharField(required=True)

    class Meta:
        model = Perennial
        fields = ["plant_id",
                  "plant_type",
                  "plant_name",
                  "plant_size",
                  "plant_color",
                  "plant_description",
                  "plant_picture",
                  "department_id", ]

    def create(self, validated_data):
        plant = Perennial.objects.create(
            plant_type=validated_data['plant_type'],
            plant_name=validated_data['plant_name'],
            plant_size=validated_data['plant_size'],
            plant_color=validated_data['plant_color'],
            plant_description=validated_data['plant_description'],
            plant_picture=validated_data['plant_picture'],
            department_id=validated_data['department_id']
        )
        return plant


class CreateShrubSerializer(serializers.ModelSerializer):
    department_id = serializers.CharField(required=True)
    plant_color = serializers.CharField(required=True)
    plant_description = serializers.CharField(required=True)
    plant_name = serializers.CharField(required=True)
    plant_picture = serializers.ImageField(required=False)
    plant_size = serializers.CharField(required=True)
    plant_type = serializers.CharField(required=True)

    class Meta:
        model = Shrub
        fields = ["plant_id",
                  "plant_type",
                  "plant_name",
                  "plant_size",
                  "plant_color",
                  "plant_description",
                  "plant_picture",
                  "department_id", ]

    def create(self, validated_data):
        plant = Shrub.objects.create(
            plant_type=validated_data['plant_type'],
            plant_name=validated_data['plant_name'],
            plant_size=validated_data['plant_size'],
            plant_color=validated_data['plant_color'],
            plant_description=validated_data['plant_description'],
            plant_picture=validated_data['plant_picture'],
            department_id=validated_data['department_id']
        )
        return plant


class CreateTreeSerializer(serializers.ModelSerializer):
    department_id = serializers.CharField(required=True)
    plant_color = serializers.CharField(required=True)
    plant_description = serializers.CharField(required=True)
    plant_name = serializers.CharField(required=True)
    plant_picture = serializers.ImageField(required=False)
    plant_size = serializers.CharField(required=True)
    plant_type = serializers.CharField(required=True)

    class Meta:
        model = Tree
        fields = ["plant_id",
                  "plant_type",
                  "plant_name",
                  "plant_size",
                  "plant_color",
                  "plant_description",
                  "plant_picture",
                  "department_id", ]

    def create(self, validated_data):
        plant = Tree.objects.create(
            plant_type=validated_data['plant_type'],
            plant_name=validated_data['plant_name'],
            plant_size=validated_data['plant_size'],
            plant_color=validated_data['plant_color'],
            plant_description=validated_data['plant_description'],
            plant_picture=validated_data['plant_picture'],
            department_id=validated_data['department_id']
        )
        return plant
