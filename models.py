from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Post(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    feedback = models.CharField(max_length=200)    

    def __str__(self):
        return self.name
# Create your models here.
