from django.db import models
from .fields import ColorField


class Product(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField()

    def __str__(self):
        return self.name
