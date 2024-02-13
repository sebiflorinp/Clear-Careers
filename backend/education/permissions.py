from rest_framework.permissions import BasePermission
from .serializers import EducationSerializer


class IsEducationOwner(BasePermission):
    def has_object_permission(self, request, view, education):
        education_data = EducationSerializer(education).data
        if request.data['employee_id'] == education_data['employee_id']:
            return True
        return False
