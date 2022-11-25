from django.db import models
from users.models import CustomUserModel
from commons.models import createdModel, deletedModel
# Create your models here.


class Student(CustomUserModel, createdModel, deletedModel):
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []