from django.db import models
from django.contrib.auth.models import AbstractUser
from about.models import Region


# Create your models here.

class UserModel(AbstractUser):
    photo = models.ImageField(upload_to='users_image/', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=256)
    gender = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class School(models.Model):
    school_name = models.CharField(max_length=20)
    number = models.PositiveIntegerField()
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)


class Participant(models.Model):
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Expert(models.Model):
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="account/media", null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    last_checked_competition = models.PositiveIntegerField(null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

