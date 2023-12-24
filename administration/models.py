from django.db import models
from account.models import UserModel


# Create your models here.
class AdminModel(models.Model):
    rules = models.CharField(max_length=100)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class RuleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    admin_site = models.ForeignKey(AdminModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'