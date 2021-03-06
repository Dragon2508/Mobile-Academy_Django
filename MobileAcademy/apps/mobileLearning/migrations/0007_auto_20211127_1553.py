# Generated by Django 3.1.7 on 2021-11-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLearning', '0006_auto_20211127_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_name',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Отчество'),
        ),
    ]
