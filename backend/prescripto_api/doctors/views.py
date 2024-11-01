from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Category, User
from .serializers import CategorySerializer, UserSerializer

# Create your views here.

class CategoryListView (ListAPIView): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserListView (ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id: 
            return User.objects.filter(category_id = category_id)
        return User.objects.all()



