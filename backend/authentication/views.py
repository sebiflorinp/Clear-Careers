from .models import Employer, Employee, User
from djoser.serializers import UserCreateSerializer
from .serializers import EmployerSerializer, EmployeeSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RetrieveUpdateDeleteEmployees(APIView):
    def get(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.get(employee_id=kwargs.get('employee_id'))
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.get(employee_id=kwargs.get('employee_id'))
            updated_employee = EmployeeSerializer(employee, data=request.data)
            if updated_employee.is_valid():
                updated_employee.save()
                return Response(updated_employee.data)
            else:
                return Response(updated_employee.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.get(employee_id=kwargs.get('employee_id'))
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateListEmployees(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(user_id=request.data['user_id'])
            user_data = UserSerializer(user)
            # if there is already an employee or employer created with the received return a 400
            employees = Employee.objects.filter(employee_id=request.data['user_id'])
            employers = Employer.objects.filter(employer_id=request.data['user_id'])
            if len(employees) > 0 or len(employers) > 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            request.data['employee_id'] = request.data['user_id']
            request.data['user'] = user_data.data
            employee = EmployeeSerializer(data=request.data)

            if employee.is_valid():
                employee.save()
                return Response(employee.data, status=status.HTTP_201_CREATED)
            else:
                return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateListEmployers(APIView):
    def get(self, request, *args, **kwargs):
        employers = Employer.objects.all()
        serializer = EmployerSerializer(employers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(user_id=request.data['user_id'])
            user_data = UserSerializer(user)
            # check if the received credentials have an employee / employer account already associated with
            employees = Employee.objects.filter(employee_id=request.data['user_id'])
            employers = Employer.objects.filter(employer_id=request.data['user_id'])
            if len(employees) != 0 or len(employers) != 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            # add the credentials and the employer_id to the received data
            request.data['user'] = user_data.data
            request.data['employer_id'] = request.data['user_id']
            employer = EmployerSerializer(data=request.data)
            if employer.is_valid():
                employer.save()
                return Response(employer.data)
            else:
                return Response(employer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteEmployers(APIView):
    def get(self, request, *args, **kwargs):
        try:
            employer = Employer.objects.get(employer_id=kwargs.get('employer_id'))
            serializer = EmployerSerializer(employer)
            return Response(serializer.data)
        except Employer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            employer = Employer.objects.get(employer_id=kwargs.get('employer_id'))
            updated_employer = EmployerSerializer(employer, data=request.data)
            if updated_employer.is_valid():
                updated_employer.save()
                return Response(updated_employer.data)
            else:
                return Response(updated_employer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            employer = Employer.objects.get(employer_id=kwargs.get('employer_id'))
            employer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Employer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)