from django.db import models

class DriverInfo(models.Model):
    user_id = models.IntegerField()
    driverName = models.CharField(max_length=100)
    trailerNumber = models.IntegerField()
    truckNumber = models.IntegerField()
    homeTerminal = models.TextField()
    mainOfficeAddress = models.TextField()
    carrierName = models.CharField(max_length=100)
    milesDriven = models.TextField()
    shipperCommodity = models.TextField()
    totalMileage = models.TextField()
    remarks = models.TextField()
    def __str__(self):
        return self.driverName
    
class LocationInfo(models.Model):
    user_id = models.IntegerField()
    currentLocation = models.TextField()
    pickupLocation  = models.TextField()
    dropoffLocation  = models.TextField()
    hours = (
        ('70 Hour / 8 Day','70'),
        ('60 Hour / 7 Day','60'),
    )
    currentcyclic = models.CharField(max_length=20,choices=hours,default='70', blank=False)
    def __str__(self):
        return self.currentLocation