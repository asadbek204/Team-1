from django.db import models
from account.models import UserModel, Expert, Region, Participant


# Create your models here.
class CompetitionModel(models.Model):
    title = models.CharField(max_length=100, help_text='Title For Your Image')
    description = models.TextField(help_text='Description Of It')
    photo = models.ImageField(upload_to='user_participate')

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_age = models.PositiveIntegerField()
    end_age = models.PositiveIntegerField()

    # experts
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    # regions
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'


class QuestionnaireModel(models.Model):
    first_name = models.CharField(max_length=50, help_text='Your First Name like: Ali')
    last_name = models.CharField(max_length=50, help_text='Your Family Name: Aliyev')
    age = models.PositiveIntegerField()
    file = models.FileField()
    final_score = models.PositiveIntegerField()
    # region
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    # participent
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    competition = models.ForeignKey(CompetitionModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'
