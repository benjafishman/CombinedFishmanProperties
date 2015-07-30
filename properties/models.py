from django.db import models

# Create your models here.


class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    history = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Apartment(models.Model):
    property = models.ForeignKey(Property)
    apt_num = models.CharField(max_length=200)
    vacant = models.NullBooleanField()
    number_of_rooms = models.IntegerField()

