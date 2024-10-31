from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Category, Doctor
from .serializers import CategorySerializer, DoctorSerializer

# Create your views here.

class CategoryListView (ListAPIView): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DoctorListView (ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id: 
            return Doctor.objects.filter(category_id = category_id)
        return Doctor.objects.all()



