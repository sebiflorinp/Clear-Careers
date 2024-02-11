from djoser.serializers import UserCreateSerializer
from .models import User


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'is_employer', 'is_employee', 'password']
