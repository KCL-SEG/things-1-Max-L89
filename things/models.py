from django.db import models
from django.db.models import Model


# Create your models here.
class thing(Model):
    name=models.CharField()
    description=models.TextField()
    quantity=models.IntegerField()

