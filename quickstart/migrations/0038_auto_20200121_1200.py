# Generated by Django 3.0.2 on 2020-01-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0037_auto_20200121_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='salary',
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_no',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
    ]