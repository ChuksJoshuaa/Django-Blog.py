from django.db import models
from django.urls import reverse
# Create your models here.
class sapamode(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myApp/sapa/media/')
    content = models.TextField()
    featured = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('sapa:sapa_detail', kwargs={"id": self.id})