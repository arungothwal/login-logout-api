# Generated by Django 3.0.2 on 2020-01-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0017_auto_20200117_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='request',
            field=models.BooleanField(blank=True, choices=[('approve', 'APPROVED'), ('non_approve', 'NON_APPROVED')], null=True),
        ),
    ]
