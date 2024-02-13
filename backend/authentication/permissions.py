from rest_framework.permissions import BasePermission
from .serializers import EmployeeSerializer, EmployerSerializer


class IsEmployeeAccountOwner(BasePermission):
    def has_object_permission(self, request, view, employee):
        employee_data = EmployeeSerializer(employee).data
        if request.data['employee_id'] == employee_data['employee_id']:
            return True
        return False


class IsEmployerAccountOwner(BasePermission):
    def has_object_permission(self, request, view, employer):
        employer_data = EmployerSerializer(employer).data
        if request.data['employer_id'] == employer_data['employer_id']:
            return True
        return False
