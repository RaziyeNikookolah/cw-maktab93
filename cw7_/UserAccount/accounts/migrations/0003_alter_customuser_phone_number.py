# Generated by Django 4.2.2 on 2023-06-30 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='invalid phone number', regex='^[0-9]{11}$')], verbose_name='phone number'),
        ),
    ]
