from django.db import models


class OrderStatus(models.TextChoices):
    CREATED = 'CREATED', 'Created'
    PROCESS = 'PROCESS', 'Process'
    READY = 'READY', 'Ready'
    PRINTED = 'PRINTED', 'Printed'
    DELIVERING = 'DELIVERING', 'Delivering'
    DELIVERED = 'DELIVERED', 'Delivered'


class OrderItemStatus(models.TextChoices):
    CREATED = 'CREATED', 'Created'
    PROCESS = 'PROCESS', 'Process'
    READY = 'READY', 'Ready'
    PRINTED = 'PRINTED', 'Printed'


class ComputingDeviceStatus(models.TextChoices):
    OFFLINE = 'OFFLINE', 'Offline'
    WAITING = 'WAITING', 'Waiting'
    PROCESS = 'PROCESS', 'Process'
