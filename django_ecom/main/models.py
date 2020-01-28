from django.db import models
from datetime import datetime


class Tutorials(models.Model):
    tutorial_name = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_publish = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title

