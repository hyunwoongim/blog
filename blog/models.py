from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='', null=True, blank=True)
