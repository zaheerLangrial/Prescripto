from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student

# Create your views here.

class StudentListView (ListCreateAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentEditView (RetrieveUpdateDestroyAPIView) :
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
