from django.db import models
from Accounts.models import TeacherAccount
from university.models import University
# Create your models here.from django.db import models

class Department(models.Model):
    """
    Represents a department within a university.

    Attributes:
        name (str): Name of the department.
        department_head (ForeignKey): Reference to the department head account.
        total_students (int): Total number of students in the department.
        created_at (datetime): Timestamp for when the department was created.
        updated_at (datetime): Timestamp for when the department details were last updated.
    """
    name = models.CharField(max_length=50, unique=True)
    University = models.ForeignKey(University, verbose_name=(""), on_delete=models.CASCADE)
    department_head = models.OneToOneField(
        TeacherAccount,  # Use string for circular imports if DepartmentHeadAccount isn't imported yet.
        verbose_name="Department Head",
        on_delete=models.SET_NULL,  # Use SET_NULL to avoid losing the department if the head is deleted.
        null=True,
        blank=True,
    )
    total_students = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)  # Auto-populates on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updates on save

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['name']  # Default ordering by name

    def __str__(self):
        return self.name  # Makes objects easier to identify in the admin panel


class Batch(models.Model):
    department_name = models.ForeignKey(Department, verbose_name=("department"), on_delete=models.CASCADE)
    batch_number = models.IntegerField(unique=True)
    start_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    total_students = models.IntegerField()

