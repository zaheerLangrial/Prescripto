from django.urls import path
from .views import DemoUserSignupView, DemoUserLoginView


# # last py ata ha url

urlpatterns = [ 
    # is me ham urlpatterns ko use karty huyee [] me urls bana ly gy path ko use karty huye 
    path('signup/', DemoUserSignupView.as_view()),
    path('login/', DemoUserLoginView.as_view()),
]
