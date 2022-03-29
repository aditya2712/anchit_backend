from django.urls import path, include
from .views import HealthCheckAPI

urlpatterns = [
    path("", HealthCheckAPI.as_view(), name="health_check"),
    path("contact/", include("contactus.urls")),
]
