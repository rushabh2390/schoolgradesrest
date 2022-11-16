from django.db import models

# Create your models here.
from schools.models import School
from commons.models import createdModel, deletedModel


class Student(createdModel, deletedModel):
    name = models.TextField(max_length=300)
    password = models.CharField(max_length=200)
    username = models.EmailField(max_length=200)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    
    @staticmethod
    def get_user_for_login(username, password):
        try:
            return Student.objects.get(username=username, password=password)
        except:
            return False

    @staticmethod
    def get_user(username):
        try:
            return Student.objects.get(username=username)
        except:
            return False

    @staticmethod
    def is_duplicate(username):
        try:
            return Student.objects.get(username=username)
        except:
            return False
