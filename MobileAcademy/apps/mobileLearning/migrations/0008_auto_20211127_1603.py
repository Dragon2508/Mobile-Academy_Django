# Generated by Django 3.1.7 on 2021-11-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLearning', '0007_auto_20211127_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
