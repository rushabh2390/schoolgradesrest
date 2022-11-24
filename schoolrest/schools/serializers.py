from rest_framework import serializers
from .models import School


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['name', 'email', 'password', 'city', 'pincode']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = School(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            city=self.validated_data['city'],
            pincode=self.validated_data['pincode'])
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
