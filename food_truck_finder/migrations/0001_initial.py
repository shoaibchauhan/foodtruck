# Generated by Django 5.0.6 on 2024-05-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCartDetail',
            fields=[
                ('locationid', models.AutoField(primary_key=True, serialize=False)),
                ('Applicant', models.CharField(max_length=255)),
                ('FacilityType', models.CharField(max_length=100)),
                ('cnn', models.CharField(max_length=100)),
                ('LocationDescription', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('blocklot', models.CharField(max_length=100)),
                ('block', models.CharField(max_length=100)),
                ('lot', models.CharField(max_length=100)),
                ('permit', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('FoodItems', models.TextField()),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Schedule', models.CharField(max_length=255)),
                ('dayshours', models.CharField(max_length=255)),
                ('NOISent', models.CharField(max_length=100)),
                ('Approved', models.CharField(max_length=100)),
                ('Received', models.CharField(max_length=100)),
                ('PriorPermit', models.CharField(max_length=100)),
                ('ExpirationDate', models.DateField()),
                ('Location', models.CharField(max_length=255)),
                ('FirePreventionDistricts', models.CharField(max_length=100)),
                ('PoliceDistricts', models.CharField(max_length=100)),
                ('SupervisorDistricts', models.CharField(max_length=100)),
                ('ZipCodes', models.CharField(max_length=100)),
                ('Neighborhoods', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'food_cart',
            },
        ),
    ]