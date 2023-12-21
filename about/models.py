from django.db import models
from competition.models import QuestionnaireModel
from account.models import Expert


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Result(models.Model):
    score = models.PositiveIntegerField()
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(QuestionnaireModel, on_delete=models.CASCADE)
