from django.db import models

# Create your models here.

class Car(models.Model):

    #pk
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f'Car is {self.brand}/{self.year} pk is {self.pk}'

