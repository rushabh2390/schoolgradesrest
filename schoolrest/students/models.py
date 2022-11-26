from django.db import models
from users.models import CustomUserModel
from commons.models import createdModel, deletedModel


class Student(CustomUserModel, createdModel, deletedModel):
    pass
