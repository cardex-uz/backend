from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Customer(models.Model):
    user = models.OneToOneField(verbose_name="user", to=User, on_delete=models.CASCADE)
    otp_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.user.__str__()


class Provider(models.Model):
    user = models.OneToOneField(verbose_name="user", to=User, on_delete=models.CASCADE)


class Device(models.Model):
    """ """
    imei = models.CharField(verbose_name="imei", max_length=16, unique=True)
    status = models.CharField(verbose_name="Status", max_length=10, default="OFFLINE")#, choices=COMPUTING_DEVICE_STATUS)

    class Meta:
        db_table = 'device'
        verbose_name = "Computing Device"
        verbose_name_plural = "Computing Devices"

    def __str__(self):
        return self.imei
