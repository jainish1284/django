from django.db import models
from datetime import datetime


class Tutorials(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("Published Date", default=datetime.now())

    def __str__(self):
        return self.tutorial_content

