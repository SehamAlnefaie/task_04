from django.db import models
from datetime import datetime 
# Create your models here.
class Restaurant (models.Model):

    name= models.CharField(max_length=20)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
       return self.name

