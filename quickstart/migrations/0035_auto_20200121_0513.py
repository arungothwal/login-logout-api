# Generated by Django 3.0.2 on 2020-01-21 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0034_auto_20200121_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
    ]
