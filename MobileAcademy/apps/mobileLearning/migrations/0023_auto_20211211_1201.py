# Generated by Django 3.1.7 on 2021-12-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLearning', '0022_auto_20211209_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscourse',
            name='test_status',
            field=models.CharField(default='не начат', max_length=100, verbose_name='Статус теста'),
        ),
    ]
