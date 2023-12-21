from django.db import models


# Create your models here.
class AdminModel(models.Model):
    # user
    rules = models.CharField()


class RuleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    admin_site = models.ForeignKey(AdminModel, on_delete=models.CASCADE)
