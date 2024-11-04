from rest_framework import serializers
from .models import DemoUser

class DemoUserSerializer(serializers.ModelSerializer): 
    # serializer class se hi start huga or is k under bi class hi lagai jati abi tak ki samj k motabik
    class Meta : 
        model = DemoUser
        # model equal to created model
        fields = '__all__'
        # fields equal to jo jo fields chahiye aghar selected field chahiye to fir bhari brackits me un ki keys ko likhna huga string me jese array likhty huty 
        # Aghar sari chahiye to fir yeh simple triqa ha all wala 