from rest_framework import serializers
from .models import DriverInfo, LocationInfo


class DriverInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverInfo
        fields = '__all__'


class LocationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = '__all__'