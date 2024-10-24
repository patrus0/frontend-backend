from django.urls import path 
from .views import *

urlpatterns=[
    path('create/', BookCreateAPIView.as_view())
]