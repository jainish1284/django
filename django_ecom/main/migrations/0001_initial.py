# Generated by Django 3.0.2 on 2020-01-23 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=200)),
                ('tutorial_content', models.TextField()),
                ('tutorial_publish', models.DateTimeField(default=datetime.datetime(2020, 1, 23, 6, 14, 38, 509762), verbose_name='date published')),
            ],
        ),
    ]
