# Generated by Django 2.2.7 on 2020-03-03 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_tools', '0004_auto_20200303_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='establish_date',
            field=models.IntegerField(default=1, max_length=4, validators=[django.core.validators.MaxLengthValidator(9999)]),
        ),
    ]
