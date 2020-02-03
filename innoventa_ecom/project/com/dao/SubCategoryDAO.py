from django.db import models
from project.com.dao import con_db


class homePageModel(models.Model):
    homePageName = models.CharField(max_length=200)
    homePageDescription = models.CharField(max_length=200)
    connection = con_db()
    result = connection.execute('select * from user')


