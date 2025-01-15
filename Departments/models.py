from django.utils import timezone

from django.db import models
from Accounts.models import TeacherAccount
from university.models import University
# Create your models here.from django.db import models
class Department(models.Model):
    """
    Represents a department within a university.

    Attributes:
        name (str): Name of the department.
        department_head (OneToOneField): Reference to the department head account.
        total_students (int): Total number of students in the department.
        created_at (datetime): Timestamp for when the department was created.
        updated_at (datetime): Timestamp for when the department details were last updated.
    """
    name = models.CharField(max_length=50, unique=True)
    university = models.ForeignKey(University, verbose_name="University", on_delete=models.CASCADE,default=1)
    department_head = models.OneToOneField(
        "Accounts.TeacherAccount",
        verbose_name="Department Head",
        on_delete=models.SET_NULL,  # Prevent department deletion if the head is deleted.
        null=True,
        blank=True,
    )
    total_students = models.PositiveIntegerField(default=0)  # Optional: Dynamically calculate this.
    created_at = models.DateField(null=False, blank = False)# Automatically set when created.
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on every save.

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['name']  # Default ordering by name.

    def __str__(self):
        return f"{self.name} ({self.university.name})"

    @property
    def student_count(self):
        """
        Dynamically calculate the total number of students in the department.
        Assumes a related `Student` model with a foreign key to `Department`.
        """
        return self.students.count()  # Replace `students` with the related name in the Student model.
class Batch(models.Model):
    """
    Represents a batch within a department.

    Attributes:
        department (ForeignKey): Reference to the associated department.
        batch_number (int): Unique identifier for the batch.
        start_date (datetime): Start date of the batch.
        end_date (datetime): End date of the batch.
        total_students (int): Number of students in the batch.
    """
    department = models.ForeignKey(Department, verbose_name="Department", on_delete=models.CASCADE,default=1)
    batch_number = models.IntegerField()  # Remove `unique=True` if using the unique constraint below.
    start_date = models.DateField(null=False, blank = False)
    end_date = models.DateField(editable=False) 
    total_students = models.IntegerField()

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"
        ordering = ['start_date']
        unique_together = ('department', 'batch_number')  # Ensure unique batch numbers per department.
    def save(self, *args, **kwargs):
        """
        Automatically set the end_date to exactly 4 years after the start_date.
        """
        if self.start_date:  # Ensure start_date is set before calculating end_date
            self.end_date = self.start_date.replace(year=self.start_date.year + 4)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Batch {self.batch_number} ({self.department.name})"
