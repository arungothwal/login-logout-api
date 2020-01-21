# Generated by Django 3.0.2 on 2020-01-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0030_remove_myuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
    ]