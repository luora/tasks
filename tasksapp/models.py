from email.mime import image
from turtle import title
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
    

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.FileField(blank = True,)
    # file = models.FileField(up)