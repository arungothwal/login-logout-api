# Generated by Django 3.0.2 on 2020-01-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_auto_20200116_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
