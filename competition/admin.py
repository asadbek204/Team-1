from django.contrib import admin
from .models import CompetitionModel, QuestionnaireModel


# Register your models here.
@admin.register(CompetitionModel)
class CompetitionModelAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(QuestionnaireModel)
class QuestionnaireModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
