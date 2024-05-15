from datetime import date

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
        print(validated_data)
        print("department: ", validated_data['department_id'])
        d = Department.objects.get(department_id=validated_data['department_id'])
        plant = Plant(
            plant_type=validated_data['plant_type'],
            plant_name=validated_data['plant_name'],
            plant_size=validated_data['plant_size'],
            plant_color=validated_data['plant_color'],
            plant_description=validated_data['plant_description'],
            plant_picture=validated_data['plant_picture'],
            department_id=d,
        )
        return plant


class CreateAnnualSerializer(serializers.ModelSerializer):
    annual_category = serializers.CharField(required=True)
    drought_tolerant = serializers.BooleanField(required=True)
    heat_tolerant = serializers.BooleanField(required=True)
    is_hardy = serializers.BooleanField(required=True)
    is_semi_hardy = serializers.BooleanField(required=True)
    plant = serializers.CharField(required=True)
    shade_tolerant = serializers.BooleanField(required=True)

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
        print(validated_data)
        p = Plant.objects.get(plant_id=validated_data['plant'])
        plant = Annual.objects.create(
            plant=p,
            is_hardy=validated_data['is_hardy'],
            is_semi_hardy=validated_data['is_semi_hardy'],
            shade_tolerant=validated_data['shade_tolerant'],
            heat_tolerant=validated_data['heat_tolerant'],
            drought_tolerant=validated_data['drought_tolerant'],
            annual_category=validated_data['annual_category'],
        )
        plant.save()
        return plant


class CreatePerennialSerializer(serializers.ModelSerializer):
    care_level = serializers.CharField(required=True)
    light_code = serializers.CharField(required=True)
    moisture_level = serializers.CharField(required=True)
    perennial_category = serializers.CharField(required=False)
    plant = serializers.CharField(required=True)

    class Meta:
        model = Perennial
        fields = ["plant",
                  "light_code",
                  "moisture_level",
                  "care_level",
                  "perennial_category"]

    def create(self, validated_data):
        p = Plant.objects.get(plant_id=validated_data['plant'])
        plant = Perennial.objects.create(
            plant=p,
            light_code=validated_data['light_code'],
            moisture_level=validated_data['moisture_level'],
            care_level=validated_data['care_level'],
            perennial_category=validated_data['perennial_category']
        )
        plant.save()
        return plant


class CreateShrubSerializer(serializers.ModelSerializer):
    plant = serializers.CharField(required=True)
    shrub_category = serializers.CharField(required=True)

    class Meta:
        model = Shrub
        fields = ["plant",
                  "shrub_category"]

    def create(self, validated_data):
        p = Plant.objects.get(plant_id=validated_data['plant'])
        plant = Shrub.objects.create(
            plant=p,
            shrub_category=validated_data['shrub_category'],
        )
        plant.save()
        return plant


class CreateTreeSerializer(serializers.ModelSerializer):
    plant = serializers.CharField(required=True)
    tree_category = serializers.CharField(required=True)

    class Meta:
        model = Tree
        fields = ["plant",
                  "tree_category"]

    def create(self, validated_data):
        p = Plant.objects.get(plant_id=validated_data['plant'])
        plant = Tree.objects.create(
            plant=p,
            tree_category=validated_data['tree_category'],
        )
        plant.save()
        return plant

