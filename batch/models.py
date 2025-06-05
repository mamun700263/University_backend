from django.db import models
from datetime import date
from Departments.models import Department
from Accounts.models import zero_str
import logging

logger = logging.getLogger("batch.model")

def add_years(d, years):
    """
    Safely add years to a date, handling leap years (e.g., Feb 29).
    """
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        # If Feb 29 doesn't exist in the target year, fallback to Feb 28
        return date(d.year + years, 2, 28)

class Batch(models.Model):
    """
    Represents a batch within a department.
    
    Attributes:
        department (ForeignKey): The department this batch belongs to.
        batch_number (int): Batch identifier (unique per department).
        start_date (date): Start of academic period.
        end_date (date): Auto-set to 4 years after start_date.
        total_students (int): Total number of enrolled students.
    """

    department = models.ForeignKey(
        Department,
        verbose_name="Department",
        on_delete=models.CASCADE
    )
    short_name = models.CharField(
        max_length=5,
        unique=True,
        blank=True,
        null=True
    )
    batch_number = models.IntegerField(verbose_name="Batch Number")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date", editable=False)
    total_students = models.PositiveIntegerField(
        verbose_name="Total Students",
        default=0,
        help_text="Enter the total number of students in this batch"
    )

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"
        ordering = ["start_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["department", "batch_number"],
                name="unique_batch_per_department"
            )
        ]
    def batch_namer(self,batach_number,department_short_name):
        batach_number = zero_str(batach_number)
        return f'{department_short_name}{batach_number}'

    def save(self, *args, **kwargs):
        """
        Auto-calculate the end_date (4 years after start_date).
        """
        if self.start_date:
            self.end_date = add_years(self.start_date, 4)
            logger.debug(
                f"Calculated end_date for Batch {self.batch_number}: {self.end_date}"
            )
        self.short_name= self.batch_namer(self.batch_number,self.department.short_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Batch {self.batch_number} ({self.department.name})"
