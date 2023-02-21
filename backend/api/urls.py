from django.urls import path
from .views import TestAPI

urlpatterns = [
    path('', TestAPI.as_view())
]