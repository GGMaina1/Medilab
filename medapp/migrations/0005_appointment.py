# Generated by Django 5.1.6 on 2025-02-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0004_staff_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
