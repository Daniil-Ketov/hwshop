from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hardware.views import HardwareViewSet, HardwareTypeViewSet


router = DefaultRouter()
router.register('hardware', HardwareViewSet, basename='hardware')
router.register('hwtype', HardwareTypeViewSet, basename='hwtype')

urlpatterns = [
    path('', include(router.urls)),
]
