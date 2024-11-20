from django.db import models
from Accounts.models import DepartmentHeadAccount
# Create your models here.
class Department(models.Model):
    name = models.CharField( max_length=50)
    department_head = models.OneToOneField(DepartmentHeadAccount, verbose_name=("head"), on_delete=models.CASCADE)
    total_students= models.IntegerField()


class Batch(models.Model):
    department_name = models.ForeignKey(Department, verbose_name=("department"), on_delete=models.CASCADE)
    batch_number = models.IntegerField(unique=True)
    start_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    total_students = models.IntegerField()

