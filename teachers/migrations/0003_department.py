# Generated by Django 2.2.7 on 2020-03-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200222_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]