from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField( max_length=50)
    batch=models.CharField(max_length=40)
    