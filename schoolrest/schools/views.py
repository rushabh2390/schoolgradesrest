from attr import field
from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import serializers



class SchoolSeializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email')

class SchoolsApiView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializers_class = SchoolSeializer

    def get_object(self):
        return self.request.user