from django.db import models
from django.urls import reverse
# Create your models here.

class product(models.Model):
     name        = models.CharField(max_length=120)
     Description = models.TextField(blank=True, null=True)
     Prices      = models.DecimalField(decimal_places=2, max_digits=10000)
     Summary     = models.TextField()
     featured    = models.BooleanField(default=True)

     def get_absolute_url(self):
          return reverse("product:product_lay", kwargs={"id": self.id})