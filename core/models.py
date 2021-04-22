from django.db import models
import math

# Create your models here.

class Pessoa(models.Model):
    name = models.CharField(max_length=100 )
    adress = models.CharField(max_length=200 )
    cellphone = models.CharField(max_length=20 )
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50 )
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    owner = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    carPlater = models.CharField(max_length=7 )
    color = models.CharField(max_length=15 )
    description = models.TextField()
    def __str__(self):
        return self.brand.name + '-' + self.carPlater
     

class Parameters(models.Model):
    value_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    value_per_mounth = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return "Parametros"


class MoveRotate(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    value_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    
    def total_hour(self):
        total = math.ceil((self.checkout - self.checkin).total_seconds() / 3600 ) 
        return total

    def total(self):
        return (self.value_per_hour * self.total_hour())
    
    def __str__(self):
        return self.vehicle.carPlater