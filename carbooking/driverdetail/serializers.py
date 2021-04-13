from rest_framework import serializers
from .models import Driver_Registration, Driver_location
import re

class DriverRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver_Registration
        fields = ('id','name','email','phone_number','license_number','car_number')

    # field validation for  Phone_number
    def validate_phone_number(self,value):                 
        Pattern = re.compile("^[6789][0-9]{9}")
        value = str(value)
        if Pattern.match(value) is None:
            raise serializers.ValidationError('Invalid Mobile Number!!')
        return value


class DriverLocationSerializer(serializers.ModelSerializer):
    # driver = serializers.CharField(source='driver.name')
    class Meta:
        model = Driver_location
        fields = ('id','driver','latitude','longitude')

class DriverInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver_Registration
        fields = '__all__'
    
class GetAvailableCabSerializer(serializers.Serializer):

    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def validate(self, data):
        return data