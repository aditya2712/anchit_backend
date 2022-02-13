from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings


class ContactUsCreate(APIView):
    class input_serializer(serializers.Serializer):
        name = serializers.CharField(max_length=100)
        email = serializers.EmailField()
        message = serializers.CharField(max_length=4096)

    def post(self, request, format=None):
        # request_body = request.data
        serializer = self.input_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data["email"]
            name = serializer.data["name"]
            message = serializer.data["message"]
            final_message = f"Email: {email} \nName: {name} \nMessage: {message}"
            email_subject = f"New contact: {email}: {name}"
            email_message = final_message
            send_mail(
                email_subject,
                email_message,
                settings.CONTACT_EMAIL,
                settings.ADMIN_EMAIL,
            )
            return Response({"message": "Successfuly sent email"})


# Sample request body
# {
#     "name": "John Doe",
#     "email": "johndoe@sender.com",
#     "message": "Hello, this is a test message"
# }
