from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('navbar.urls')),
    path('', include('doctors.urls')),
    path('admin/', admin.site.urls),
]


