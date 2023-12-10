from django.db import models


# Create your models here.
class GalleryModel(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

