from rest_framework import serializers

from management.models import User, Customer, Provider, Device


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('date_joined', 'last_login')


class CustomSerializer(UserSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
