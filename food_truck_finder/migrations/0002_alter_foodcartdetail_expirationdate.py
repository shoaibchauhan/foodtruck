# Generated by Django 5.0.6 on 2024-05-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_truck_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcartdetail',
            name='ExpirationDate',
            field=models.DateTimeField(),
        ),
    ]
