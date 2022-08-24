from django.conf import settings
from django.db import models

# Create your models here.
class Feedback(models.Model):
    '''Feedback about'''
    text = models.CharField(max_length = 5000, verbose_name="Feedback")
    grade = models.IntegerField(verbose_name="Grade")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, verbose_name="Object")
