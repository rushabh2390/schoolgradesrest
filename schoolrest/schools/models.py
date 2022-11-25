from django.db import models
from users.models import CustomUserModel
from commons.models import createdModel, deletedModel
# Create your models here.


class School(CustomUserModel, createdModel, deletedModel):
    city = models.CharField(max_length=200, default=None)
    pincode = models.CharField(max_length=200, default=None)