from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Time(models.Model):
    time = models.CharField(max_length=30)

    def __str__(self):
        return self.time


class Date(models.Model):
    year = models.IntegerField(default=2017)
    month = models.IntegerField()
    day = models.IntegerField()
    pickup_location = models.ManyToManyField(Location)
    pickup_time = models.ManyToManyField(Time)

    def __str__(self):
        return str(self.month) + "-" + str(self.day) + "-" + str(self.year)