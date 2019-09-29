from rest_framework import routers
from .views import UserViewSet, GroupViewSet, VisitViewSet, VisitViewSetAPI
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'visit_set', VisitViewSet)


urlpatterns = [
    path(r'visitAPI/', VisitViewSetAPI.as_view()),
    path('', include(router.urls)),
]