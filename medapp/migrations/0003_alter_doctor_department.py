# Generated by Django 5.1.6 on 2025-02-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0002_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(max_length=59),
        ),
    ]
