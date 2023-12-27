from django.db import models
from django.contrib.auth.models import AbstractUser
from about.models import Region


# Create your models here.

class UserModel(AbstractUser):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    photo = models.ImageField(upload_to='users_image/', null=True, blank=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class School(models.Model):
    school_name = models.CharField(max_length=20)
    number = models.PositiveIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Participant(models.Model):
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Expert(models.Model):
    about = models.TextField()
    image = models.ImageField(upload_to="account/media")
    expert_token = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    last_checked_competition = models.PositiveIntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

