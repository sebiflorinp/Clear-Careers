from djoser.serializers import UserCreateSerializer
from .models import User, Employee, Employer
from rest_framework import serializers


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'is_employer', 'is_employee', 'password']


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employer
        fields = '__all__'
