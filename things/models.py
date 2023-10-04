from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.TextField(unique=False, blank=True, max_length=120)
    quantity = models.PositiveIntegerField(default=1, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])