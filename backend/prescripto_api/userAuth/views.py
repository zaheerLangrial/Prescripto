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
    # //Phely class banaye gy 
    def post (self, request) : 
        # Fir function post method k sath start kary gay
        user_name = request.data.get('user_name')
        # Username get kary ga request.data.get kar k 
        password = request.data.get('password')
        # then fir password get kary gy yeh bi request.data.get se aye ga matlab payload me aye ga

        user = DemoUser.objects.filter(user_name= user_name).first()
        # jab dono chezy ajye gi fir ham user ko filter kary gay model me se model .objects.filter kar k


        if user and  check_password(password, user.password): 
            # edr fir check kary gy user ha k ni or sath yeh bi check kary gy k password same ha checkpassword method ko use karty huye 
            refresh = RefreshToken.for_user(user)
            # then ham ik refreash token create kary gy RefreshToken lab ko use karty huye 
            return Response({
                "refresh": str(refresh),
                "access" : str(refresh.access_token),
            }, status=status.HTTP_200_OK)
            # yaha par fir return kar de gy tokens ko or status 200 ka kar de gy 

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        # Edr fir aghar if wali conditon true ni huti to fir yeh return kar de ga
        # esy mazeed me better kar skta hun lkn samjne k liye yeh bht ha 

