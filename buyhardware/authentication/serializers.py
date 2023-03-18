from rest_framework import serializers
from authentication.models import User, Client, Manager


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('login', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ('user_id', )


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        exclude = ('user_id', )


