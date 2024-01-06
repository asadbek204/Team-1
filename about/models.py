from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)


class Result(models.Model):
    score = models.PositiveIntegerField()
    expert = models.ForeignKey('user_account.Expert', on_delete=models.CASCADE)
    questionnaire = models.ForeignKey('competition.QuestionnaireModel', on_delete=models.CASCADE)


class CounterModel(models.Model):
    criteria = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to="criteria/")
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.criteria

    class Meta:
        verbose_name = "counter"
        verbose_name_plural = "counters"
        db_table = "counter"


class AdvantagesModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="advantages/")
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "advantage"
        verbose_name_plural = "advantages"
        db_table = "advantages"
