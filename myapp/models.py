from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Marks = models.CharField(max_length=4)