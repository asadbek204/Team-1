# Generated by Django 5.0 on 2024-01-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
