from rest_framework import serializers
from .models import Category, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ['id', 'name', 'icon']


class UserSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    image = serializers.ImageField()
    class Meta: 
        model = User
        fields = ['id', 'name', 'category', 'image','experience','role', 'is_active']