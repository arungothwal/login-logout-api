# Generated by Django 3.0.2 on 2020-01-17 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0013_auto_20200117_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_userr', to=settings.AUTH_USER_MODEL),
        ),
    ]
