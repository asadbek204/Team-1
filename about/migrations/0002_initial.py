# Generated by Django 4.2.5 on 2023-12-28 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
        ('about', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.expert'),
        ),
        migrations.AddField(
            model_name='result',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.questionnairemodel'),
        ),
    ]