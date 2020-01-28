from django.db import models
from datetime import datetime


class MainModel(models.Model):
    names = models.CharField(max_length=200)

    class Meta:
        db_table = 'demo_table'

    def __str__(self):
        return self.name


