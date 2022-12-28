from django.db import models

# Create your models here.

class Detail(models.Model):
    detail = models.JSONField()