from django.db import models


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





