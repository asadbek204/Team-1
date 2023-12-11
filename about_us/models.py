from django.db import models


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


class ExpertsModel(models.Model):
    image = models.ImageField(upload_to="experts/")
    profession = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.profession

    class Meta:
        verbose_name = "expert"
        verbose_name_plural = "experts"
        db_table = "experts"
