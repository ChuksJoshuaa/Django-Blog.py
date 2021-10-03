from django.db import models

# Create your models here.
class game(models.Model):
    server = models.CharField(max_length=100)
    gametype = models.TextField(max_length=150)
    price = models.DecimalField(decimal_places=1, max_digits=100)
    featured = models.BooleanField(default=True)



