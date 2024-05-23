from django.db.models import TextChoices


class ComputingDeviceStatus(TextChoices):
    OFFLINE = 'OFFLINE'
    WAITING = 'WAITING'
    PROCESS = 'PROCESS'
