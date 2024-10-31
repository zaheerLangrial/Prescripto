from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NavbarItems
from .serializers import NavbarItemSerializer

# Create your views here.


class NavbarListView (APIView):
    def get(self, request):
        items = NavbarItems.objects.all()
        serializer = NavbarItemSerializer(items, many=True)
        return Response(serializer.data)


# Hero Section API View
class HeroSectionView(APIView):
    def get(self, request):
        data = {
            "title": "Book Appointment With Trusted Doctors",
            "buttonText": "Book Appointment",
            "imageUrl": "../assets/doc-header-img.jpg",
        }
        return Response(data)


