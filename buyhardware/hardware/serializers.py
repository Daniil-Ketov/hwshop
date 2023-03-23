from rest_framework.serializers import ModelSerializer
from hardware.models import Hardware, HardwareType


class HardwareSerializer(ModelSerializer):
    class Meta:
        model = Hardware
        fields = "__all__"


class HardwareTypeSerializer(ModelSerializer):

    class Meta:
        model = HardwareType
        fields = "__all__"
