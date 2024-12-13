from django.db import models
from Departments.models import Department
# Create your models here.

class University(models.Model):

    name = models.CharField(max_length=50)
    departments = models.maToManyField("app.Model", verbose_name=(""))
    