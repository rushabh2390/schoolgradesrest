from django.db import models
from commons.models import createdModel, deletedModel


class Standard(createdModel, deletedModel):
    std = models.IntegerField()

    @staticmethod
    def is_duplicate(std):
        try:
            return Standard.objects.get(std=std)
        except:
            return False

    def __str__(self) -> str:
        return str(self.std)