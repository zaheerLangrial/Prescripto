from rest_framework import serializers
from .models import Category, Doctor


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ['id', 'name', 'icon']


class DoctorSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    image = serializers.ImageField()
    class Meta: 
        model = Doctor
        fields = ['id', 'name', 'category', 'image', 'is_active']