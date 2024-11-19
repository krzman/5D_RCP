from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rfid_number = models.IntegerField(unique=True, blank=False, null=False)


class RCPDevice(models.Model):
    nr = models.IntegerField(unique=True, blank=False, null=False)


class Construcion(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    city = models.CharField(max_length=64, blank=False, null=False)
    manager = models.OneToOneField(Users, on_delete=models.CASCADE)
    rfid_device = models.ForeignKey(RCPDevice, on_delete=models.CASCADE)


# class TOYOTA(models.Model):
#     construcion = models.OneToOneField(Construcion, on_delete=models.CASCADE)
#     user = models.ManyToManyField(User, on_delete=models.CASCADE)
#     date = models.DateField(blank=False, null=False, auto_now_add=True)
#     time = models.TimeField(blank=False, null=False, auto_now_add=True)
