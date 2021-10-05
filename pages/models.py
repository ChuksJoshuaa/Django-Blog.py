from django.db import models
from django.shortcuts import reverse
# Create your models here.

class page(models.Model):
    title = models.CharField(max_length=100)
    section = models.CharField(max_length=200)
    mode = models.DecimalField(decimal_places=2, max_digits=10000)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("pages:page_object", kwargs={"id": self.id})        #f"/pages/{{self.id}}/"