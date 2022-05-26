from django.db import models

# Create your models here.


class Doctor(models.Model):
    full_name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
