from django.db import models


class ExpertModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "expert"
        verbose_name_plural = "experts"
        db_table = "experts"

