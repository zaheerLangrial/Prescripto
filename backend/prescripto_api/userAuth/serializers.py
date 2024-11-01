from rest_framework import serializers
from .models import DemoUser

class DemoUserSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = DemoUser
        fields = '__all__'