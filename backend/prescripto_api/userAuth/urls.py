from django.urls import path
from .views import DemoUserSignupView, DemoUserLoginView

urlpatterns = [
    path('signup/', DemoUserSignupView.as_view()),
    path('login/', DemoUserLoginView.as_view()),

]
