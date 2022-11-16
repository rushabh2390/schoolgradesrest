from django.db import models
from commons.models import createdModel, deletedModel


# Create your models here.


class Subject(createdModel, deletedModel):
    subject_name = models.CharField(max_length=50)


    @staticmethod
    def is_duplicate(subject_name):
        try:
            return Subject.objects.get(subject_name=subject_name)
        except:
            return False

    def __str__(self) -> str:
        return self.subject_name