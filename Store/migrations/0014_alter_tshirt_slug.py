# Generated by Django 3.2.9 on 2021-11-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_tshirt_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
