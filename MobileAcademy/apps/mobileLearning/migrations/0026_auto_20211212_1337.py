# Generated by Django 3.1.7 on 2021-12-12 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLearning', '0025_auto_20211211_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 12, 13, 37, 57, 751294), verbose_name='Дата рождения'),
        ),
    ]