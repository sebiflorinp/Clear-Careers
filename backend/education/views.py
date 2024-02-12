from .models import Education
from authentication.models import Employee
from .serializers import EducationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CreateEducation(APIView):
    def post(self, request, *args, **kwargs):
        # Check if the employer_id is valid
        try:
            employee_id = kwargs.get('employee_id')
            employee = Employee.objects.get(employee_id=employee_id)
            # Create the instance
            request.data['employee_id'] = employee_id
            education = EducationSerializer(data=request.data)
            if education.is_valid():
                education.save()
                return Response(education.data)
            else:
                return Response(education.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteEducation(APIView):
    def put(self, request, *args, **kwargs):
        # Check if the education with the input id exists
        try:
            education = Education.objects.get(education_id=kwargs.get('education_id'))

            updated_education = EducationSerializer(education, data=request.data)
            if updated_education.is_valid():
                updated_education.save()
                return Response(updated_education.data)
            else:
                return Response(updated_education.errors, status=status.HTTP_400_BAD_REQUEST)
        except Education.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)