from django.db import models


# Create your models here.

class Car(models.Model):
    # pk
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f'Car is {self.brand}/{self.year} pk is {self.pk}'


class Review_stars(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    stars = models.IntegerField()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'Rewiev for {self.first_name}/{self.last_name} does {self.stars} star(s)'

