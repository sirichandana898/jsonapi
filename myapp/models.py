from django.db import models

class Students(models.Model):
    Name = models.CharField(max_length=100)
    Marks = models.CharField(max_length=4)