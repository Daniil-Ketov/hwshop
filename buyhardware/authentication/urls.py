from django.urls import path

from .views import UserAPIView, ClientAPIView, ManagerAPIView

app_name = 'core'

urlpatterns = [
    path('register/', UserAPIView.as_view(), name="register"),
    path('profile/', UserAPIView.as_view(), name='profile'),
    path('profile/client/', ClientAPIView.as_view(), name='client profile'),
    path('managers/<int:pk>/', ManagerAPIView.as_view(), name='managers')
]
