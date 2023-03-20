from rest_framework.viewsets import ModelViewSet
from hardware.models import Hardware
from hardware.serializers import HardwareSerializer


class HardwareViewSet(ModelViewSet):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer
