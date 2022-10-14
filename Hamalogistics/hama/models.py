from django.db import models
from django.contrib.auth.models import User
#from django.utils.translation import ugettext as _

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=80, null=True)
    email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    lastName = models.CharField(max_length=20, null=True)
    firstName = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=80, null=True)
    email = models.CharField(max_length=30, null=True)
    jobTitle = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.lastName

class Vehicle(models.Model):
    vehicle_status = (('available', 'available'),
    ('booked', 'booked'))
    RegNo = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=255, null=True)
    model=models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255, null=True)
    capacity = models.CharField(max_length=10, null=True)
    charges=models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=200, null=True, choices=vehicle_status)

    def __str__(self):
        return self.type


class Book_Vehicle(models.Model):
    RegNo=models.ForeignKey(Vehicle,null=True,on_delete=models.CASCADE)

