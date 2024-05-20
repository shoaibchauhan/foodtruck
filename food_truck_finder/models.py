from django.db import models


# Create your models here.

class FoodCartDetail(models.Model):
    locationid = models.AutoField(primary_key=True)
    Applicant = models.CharField(max_length=255,null=True,blank=True)
    FacilityType = models.CharField(max_length=100,null=True,blank=True)
    cnn = models.CharField(max_length=100,null=True,blank=True)
    LocationDescription = models.CharField(max_length=255,null=True,blank=True)
    Address = models.CharField(max_length=255,null=True,blank=True)
    blocklot = models.CharField(max_length=100,null=True,blank=True)
    block = models.CharField(max_length=100,null=True,blank=True)
    lot = models.CharField(max_length=100,null=True,blank=True)
    permit = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(max_length=100,null=True,blank=True)
    FoodItems = models.TextField(null=True,blank=True)
    X = models.FloatField(null=True,blank=True)
    Y = models.FloatField(null=True,blank=True)
    Latitude = models.FloatField(null=True,blank=True)
    Longitude = models.FloatField(null=True,blank=True)
    Schedule = models.CharField(max_length=255,null=True,blank=True)
    dayshours = models.CharField(max_length=255,null=True,blank=True)
    NOISent = models.CharField(max_length=100,null=True,blank=True)
    Approved = models.CharField(max_length=100,null=True,blank=True)
    Received = models.CharField(max_length=100,null=True,blank=True)
    PriorPermit = models.CharField(max_length=100,null=True,blank=True)
    ExpirationDate = models.DateTimeField(null=True,blank=True)
    Location = models.CharField(max_length=255,null=True,blank=True)
    FirePreventionDistricts = models.CharField(max_length=100,null=True,blank=True)
    PoliceDistricts = models.CharField(max_length=100,null=True,blank=True)
    SupervisorDistricts = models.CharField(max_length=100,null=True,blank=True)
    ZipCodes = models.CharField(max_length=100,null=True,blank=True)
    Neighborhoods = models.CharField(max_length=255,null=True,blank=True)

    class Meta:
        db_table = "food_cart"
