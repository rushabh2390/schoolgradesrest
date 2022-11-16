from django.db import models
from commons.models import createdModel, deletedModel
# Create your models here.


class School(createdModel, deletedModel):
    name = models.TextField(max_length=300)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)

    @staticmethod
    def get_user_for_login(email, password):
        try:
            return School.objects.get(email=email, password=password)
        except:
            return False

    @staticmethod
    def get_user(email):
        try:
            return School.objects.get(email=email)
        except:
            return False

    @staticmethod
    def is_duplicate(email):
        try:
            return School.objects.get(email=email)
        except:
            return False

    def __str__(self) -> str:
        return self.name