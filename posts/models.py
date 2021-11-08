from django.urls import reverse
from django.core.files.storage import default_storage as storage
from django.db import models
from django.utils import timezone
from PIL import Image
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class postmode(models.Model):
    image = models.ImageField(upload_to='myApp/posts/media/', null=False, blank=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title and self.content:
            return

        super(postmode, self).save()
        if self.image:
            size = 200, 200
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = 'png'  # You need to set the correct image format here
            image.save(fh, format)
            fh.close()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"id": self.id})

class Comment(models.Model):
    post = models.ForeignKey(postmode, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return 'Comment {}'.format(self.commenter_name)
