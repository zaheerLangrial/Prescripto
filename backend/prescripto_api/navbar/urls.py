from django.urls import path 
from .views import NavbarListView, HeroSectionView

urlpatterns = [
    path('navbar/', NavbarListView.as_view()),
    path('herosection/', HeroSectionView.as_view())
]
