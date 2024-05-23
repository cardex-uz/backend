from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .choices import ComputingDeviceStatus
from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    """ """
    avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars/", default=settings.NO_AVATAR)
    phone = models.CharField(verbose_name="Phone Number", max_length=15, unique=True)
    verify_time = models.DateTimeField(verbose_name="Verify Time", default=timezone.now)
    created_at = models.DateTimeField(verbose_name="Created Time", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated Time", auto_now=True)

    email = None
    groups = None
    user_permissions = None

    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        self.username = self.phone
        super().save(*args, **kwargs)

    # @property
    # def is_active(self):
    #     if self.verify_time < timezone.now():
    #         return False
    #     return True
    #
    # @is_active.setter
    # def is_active(self, value):
    #     self._is_active = value


class Customer(models.Model):
    user = models.OneToOneField(
        verbose_name="user", to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer"
    )

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.user.__str__()


class Provider(models.Model):
    user = models.OneToOneField(
        verbose_name="user", to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="provider"
    )


class Device(models.Model):
    """ """
    imei = models.CharField(verbose_name="imei", max_length=16, unique=True)
    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        default=ComputingDeviceStatus.OFFLINE,
        choices=ComputingDeviceStatus.choices
    )

    class Meta:
        db_table = 'device'
        verbose_name = "Computing Device"
        verbose_name_plural = "Computing Devices"

    def __str__(self):
        return self.imei

    @property
    def is_authenticated(self):
        return True

    def set_offline(self):
        self.status = ComputingDeviceStatus.OFFLINE
        super().save()

    def set_waiting(self):
        self.status = ComputingDeviceStatus.WAITING
        super().save()


class AnonymousDevice:
    from management.choices import ComputingDeviceStatus
    imei = None
    status = ComputingDeviceStatus.OFFLINE
    is_authenticated = False
