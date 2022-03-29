from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheckAPI(APIView):
    """
    Health Check API
    """

    def get(self, request):
        """
        Health Check API
        """

        return Response(data={"message": "Health Check OK"}, status=200)
