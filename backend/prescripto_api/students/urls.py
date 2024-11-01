from django.urls import path
from .views import StudentListView, StudentEditView

urlpatterns = [
    path('students', StudentListView.as_view() ),
    path('students/<int:id>/', StudentEditView.as_view())
]