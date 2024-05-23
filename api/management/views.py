from datetime import timedelta
from random import randint

from django.contrib.auth.hashers import make_password
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.management.serializers import UserSerializer, ProviderSerializer, DeviceSerializer, PhoneSerializer
from management.models import User, Customer, Provider, Device
from management.services.tasks import send_verify_code


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'login':
            self.permission_classes = [AllowAny]

        return super(UserViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == 'login':
            return PhoneSerializer
        return UserSerializer

    def get_object(self):
        if self.action == 'me':
            return self.request.user
        return super().get_object()

    @action(url_path="me", detail=False, methods=['GET', 'PUT'])
    def me(self, request, *args, **kwargs):
        match request.method:
            case "GET":
                return super().retrieve(request, *args, **kwargs)
            case "PUT":
                return super().update(request, *args, **kwargs)

    @action(url_path="login", detail=False, methods=["POST"])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone = serializer.validated_data["phone"]
            password = str(randint(1000, 9999))
            verify_time = timezone.now() + timedelta(minutes=3)
            self.queryset.update_or_create(
                phone=phone,
                defaults={
                    'password': make_password(password),
                    'verify_time': verify_time,
                    'is_active': True
                }
            )
            send_verify_code(phone, password)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
