from django.db import models

# Create your models here.

class BlogPost(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='static/posts_images/')
    date = models.DateTimeField(auto_now_add=True)
