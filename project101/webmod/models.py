from django.db import models

# Create your models here.
class Subscriber(models.Model):
    sub_name = models.CharField(max_length=100)
    sub_email = models.EmailField(max_length=100)