# Generated by Django 5.0 on 2024-01-06 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title For Your Image', max_length=100)),
                ('description', models.TextField(help_text='Description Of It')),
                ('photo', models.ImageField(upload_to='user_participate')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('start_age', models.PositiveIntegerField()),
                ('end_age', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
            },
        ),
        migrations.CreateModel(
            name='QuestionnaireModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Your First Name like: Ali', max_length=50)),
                ('last_name', models.CharField(help_text='Your Family Name: Aliyev', max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('final_score', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Questionnaire',
                'verbose_name_plural': 'Questionnaires',
            },
        ),
    ]
