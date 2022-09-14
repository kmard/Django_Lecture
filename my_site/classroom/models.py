from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    class Meta:
        verbose_name = "TEACHER"
        verbose_name_plural = "TEACHERS"

    def __str__(self):
        return f'Teacher : {self.first_name}/{self.last_name}/{self.subject}'