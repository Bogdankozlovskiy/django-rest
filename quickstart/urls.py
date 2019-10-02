from .views import VisitViewSetAPI, RegisterAPI
from django.urls import path, include


urlpatterns = [
    path(r'visitAPI/', VisitViewSetAPI.as_view()),
    path(r'register/', RegisterAPI.as_view()),
]