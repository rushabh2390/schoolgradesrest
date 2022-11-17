from django.db import models

# Create your models here.
from schools.models import School
from users.models import User
from commons.models import createdModel, deletedModel


class Student(User,createdModel, deletedModel):
    username = models.EmailField(max_length=200)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name