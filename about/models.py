from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Result(models.Model):
    #expert
    score = models.PositiveIntegerField()
