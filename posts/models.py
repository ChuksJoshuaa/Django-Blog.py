from django.urls import reverse
from django.db import models
from django.utils import timezone
from PIL import Image
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class postmode(models.Model):
    image = models.ImageField(upload_to='myApp/posts/media/', null=False, blank=False)
    title = models.CharField(max_length=60)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


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


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)

class CommentUserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   user_image = models.ImageField(default='default.jpg', upload_to='profile_pics')



class PostImage(models.Model):
    image = models.ImageField(upload_to='myApp/posts/media/')