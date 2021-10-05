from django.db import models

# Create your models here.

class school(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=4, max_digits=100000)
    featured = models.BooleanField(default=True)