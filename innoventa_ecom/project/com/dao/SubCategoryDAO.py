from django.db import models
from project.com.dao import con_db


class CategoryDAO(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=200)

    def searchCategory(self):
        print("innn")

    class Meta():
        db_table = 'categorymaster'


class SubCategoryDAO(models.Model):
    homePageName = models.CharField(max_length=200)
    homePageDescription = models.CharField(max_length=200)

    def insertSubCategory(self):
        connection = con_db()
        result = connection.execute('select * from user')
        return result

