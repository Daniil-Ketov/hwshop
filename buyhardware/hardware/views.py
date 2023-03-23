from rest_framework.viewsets import ModelViewSet
from hardware.models import Hardware, HardwareType
from hardware.permissions import IsStaffOrReadOnly
from hardware.serializers import HardwareSerializer, HardwareTypeSerializer


class HardwareViewSet(ModelViewSet):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer


class HardwareTypeViewSet(ModelViewSet):
    permission_classes = (IsStaffOrReadOnly,)
    queryset = HardwareType.objects.all()
    serializer_class = HardwareTypeSerializer
