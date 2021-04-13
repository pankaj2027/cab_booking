from django.db import models

# Create your models here.

class Driver_Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.BigIntegerField(unique=True)
    license_number = models.CharField(max_length=50, unique=True)
    car_number = models.CharField(max_length=50, unique=True)


class Driver_location(models.Model):
    driver = models.ForeignKey(Driver_Registration, on_delete = models.CASCADE, related_name ='driver')
    latitude = models.FloatField()
    longitude = models.FloatField()