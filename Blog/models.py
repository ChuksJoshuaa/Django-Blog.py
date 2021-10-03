from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(default=True)
    items = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('Blog:Blog_detail', kwargs={"id": self.id})
        #f"/Blog/{{self.id}}/"
