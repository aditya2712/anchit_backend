from django.urls import path
from contactus.views import ContactUsCreate

urlpatterns = [
    path("create/", ContactUsCreate.as_view(), name="contact-us-create"),
]
