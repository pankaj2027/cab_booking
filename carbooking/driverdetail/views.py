import geopy.distance
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Driver_location, Driver_Registration
from .serializers import (DriverLocationSerializer,
                          DriverRegistrationSerializer,
                          GetAvailableCabSerializer)


class DriverRegistration(viewsets.ViewSet):
    '''Driver registration'''

    def create(self, request):
        serializer = DriverRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            driver_data = Driver_Registration.objects.all().last()
            serializer_data = DriverRegistrationSerializer(driver_data)
            res = serializer_data.data
            return Response(res, status=status.HTTP_201_CREATED ) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        driver_list = Driver_Registration.objects.all()
        serializer = DriverRegistrationSerializer(driver_list, many=True )
        return Response(serializer.data)


class Driverlocation(viewsets.ViewSet):
    
    def create(self,request):
        serializer = DriverLocationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            driver_data = Driver_location.objects.all().last()
            serializer_data = DriverLocationSerializer(driver_data)
            res = serializer_data.data
            return Response(res, status=status.HTTP_201_CREATED ) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self,request):
        driver_list = Driver_location.objects.all()
        serializer = DriverLocationSerializer(driver_list, many=True )
        return Response(serializer.data)


class GetListOfAvailableCab(viewsets.ViewSet):

    """
    This function returns a list of available drivers, according the source address given by passenger
    Calculating available cabs is done by calculating distance between source address and available cabs location.
    If this distance is < 4 kms,  then these cabs are shown as available.
    """

    serializer_class = GetAvailableCabSerializer

    def create(self, request, format=None): 
        serializer = GetAvailableCabSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            latitude = request.data['lat']
            longitude = request.data['lon']
            driver_locations = Driver_location.objects.all()
            available_drivers_list = []

            for location in driver_locations:
                coords_1 = (latitude, longitude)
                coords_2 = (location.latitude, location.longitude)
                distance = geopy.distance.geodesic(coords_1, coords_2).km

                if distance < 4:
                    driver = location.driver_id
                    available_drivers_list.append(driver)

            if available_drivers_list:
                serializer = DriverInfoSerializer(available_drivers_list, many=True)
                return Response(serializer.data)
                
            else:
                data = {"Unavailable": "Sorry, no cabs are available at this time"}
                return Response(data)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
