from django.db import models
from commons.models import createdModel, deletedModel
from users.models import User
# Create your models here.


class School(User,createdModel, deletedModel):
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name