from enum import unique

from rest_framework import serializers
from .models import Student


class RegistrationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def get(self, request, format=None):
        users = Student.objects.all()
        serializer = UserSerializerWithToken(users, many=True)
        return Response(serializer.data)

    class Meta:
        model = Student
        fields = ['name', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Student(
            name=self.validated_data['name'],
            username=self.validated_data['username'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                {'current_password': 'Does not match'})
        return value
