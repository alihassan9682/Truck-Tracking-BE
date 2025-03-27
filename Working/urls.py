from django.urls import path
from .views import Driver, Locations

urlpatterns = [
    path("driver/",Driver.as_view(),name = "driver"),
    path("locations/", Locations.as_view() ,name = "driver")
]