from django.db import models

# Create your models here.
class Institute(models.Model):
    Institute_ID = models.IntegerField()
    Institute_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=40)
    
