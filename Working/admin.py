from django.contrib import admin
from .models import DriverInfo, LocationInfo
# Register your models here.
admin.site.register(DriverInfo)
admin.site.register(LocationInfo)