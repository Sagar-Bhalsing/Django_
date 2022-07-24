from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,default='DEFAULT VALUE')
    email= models.EmailField(max_length=140, blank=True, null=True)
    phone=models.CharField(max_length=10,default='DEFAULT VALUE')
    desc = models.TextField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.name +"-"+self.email