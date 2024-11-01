from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from .serializers import DemoUserSerializer
from .models import DemoUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

# Create your views here.


class DemoUserSignupView (APIView) : 
    def post (self, request) : 
        serializer = DemoUserSerializer(data=request.data)

        if serializer.is_valid(): 
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response({'message': 'User Created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

class DemoUserLoginView (APIView) : 
    def post (self, request) : 
        user_name = request.data.get('user_name')
        password = request.data.get('password')

        user = DemoUser.objects.filter(user_name= user_name).first()
        print(user)


        if user and  check_password(password, user.password): 
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access" : str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
