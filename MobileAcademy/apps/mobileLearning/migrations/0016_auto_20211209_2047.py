# Generated by Django 3.1.7 on 2021-12-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLearning', '0015_accesscourse_test_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscourse',
            name='test_status',
            field=models.CharField(default='Не начат', max_length=20, verbose_name='Статус теста'),
        ),
    ]
