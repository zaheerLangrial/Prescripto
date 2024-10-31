from rest_framework import serializers
from .models import NavbarItems

class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta : 
        model = NavbarItems
        fields = '__all__'