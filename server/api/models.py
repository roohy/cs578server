from django.db import models

class Status(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    info = models.CharField(max_length=100,blank=True,default='')
    user = models.IntegerField()

class USER(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=50)



# Create your models here.
