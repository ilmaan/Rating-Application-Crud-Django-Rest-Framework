from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=60)
    rating = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    review = models.CharField(max_length=500)


    def __str__(self):
        return str(self.name)
