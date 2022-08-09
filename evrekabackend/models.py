from django.db import models


class NavigationRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle = models.ForeignKey(to='vehicle', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=12)

class Bin(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Operation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Collection(models.Model):
    id = models.IntegerField(primary_key=True)
    bin = models.ForeignKey(to='bin', on_delete=models.CASCADE)
    frequency = models.IntegerField()
    last_collection = models.DateTimeField()
    operation = models.ForeignKey(to='operation', on_delete=models.CASCADE)
