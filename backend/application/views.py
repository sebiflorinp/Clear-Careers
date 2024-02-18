from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsApplicationOwnerOrReceiver
from authentication.models import User, Employer, Employee


class ListApplications(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Check if the user exists
        user_id = kwargs.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # Get the applications
        applications = Application.objects.filter(employer_id=user_id)
        if len(applications) == 0:
            applications = Application.objects.filter(employee_id=user_id)
        return Response(applications.data)


class CreateApplications(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsApplicationOwnerOrReceiver]

    def post(self, request, *args, **kwargs):
        # Check if the employer exists
        employer_id = kwargs.get('employer_id')
        try:
            Employer.objects.get(employer_id=employer_id)
            # Check if the employer_id from the request matches with the one from the endpoint
            if employer_id != request.data['employer_id']:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            application = ApplicationSerializer(data=request.data)
            # Check permissions
            self.check_object_permissions(request, application)
            # Create the application
            if application.is_valid():
                application.save()
                return Response(application.data)
            else:
                return Response(application.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
