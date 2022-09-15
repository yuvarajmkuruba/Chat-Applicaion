from email.mime import image
from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.
from embed_video.fields import EmbedVideoField
class Item(models.Model):
    Video = EmbedVideoField()
class Video(models.Model):
    Name =models.CharField(max_length=200)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.Name

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
class Feature(models.Model):
    Name=models.CharField(max_length=150)
    Details=models.CharField(max_length=2000)
    Datecreated=models.DateTimeField(default=datetime.now,blank=True)
    Image= models.ImageField(default='/blank', upload_to='images/')