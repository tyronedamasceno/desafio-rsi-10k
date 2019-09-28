from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name', 'surname', 'email', 'birth_date', 'cpf', 'password',
            'address', 'friends'
        )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}
