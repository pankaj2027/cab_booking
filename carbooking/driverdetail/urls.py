from django.urls import path,include
from rest_framework import routers
from .views import DriverRegistration,Driverlocation,GetListOfAvailableCab

router = routers.DefaultRouter()
router.register('driver/register', DriverRegistration, basename='driver_register')
router.register('driver/sendlocation', Driverlocation, basename='Driverlocation')
router.register('passenger/available_cabs', GetListOfAvailableCab, basename='GetListOfAvailableCab')


urlpatterns = [
    path('', include(router.urls)),

]