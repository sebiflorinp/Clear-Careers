from djoser.serializers import UserCreateSerializer
from .models import User, Employee, Employer
from rest_framework import serializers


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['user_id', 'email', 'password', 'is_employee', 'is_employer']
        read_only_fields = ['user_id', 'email', 'password', 'is_employee', 'is_employer']


class EmployeeSerializer(serializers.ModelSerializer):
    user_credentials = UserSerializer(read_only=True, source='employee_id')

    class Meta:
        model = Employee
        fields = '__all__'


class EmployerSerializer(serializers.ModelSerializer):
    user_credentials = UserSerializer(read_only=True, source='employer_id')

    class Meta:
        model = Employer
        fields = '__all__'
