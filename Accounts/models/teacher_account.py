import uuid
from .base_account import Account
from django.db import models

class TeacherAccount(Account, models.Model):
    """
    Teacher account with a unique ID format.
    """

    Department_head = models.BooleanField(default=False)
    department = models.ForeignKey(
        "Departments.Department",
        verbose_name="Department",
        on_delete=models.CASCADE,
        default=1,
    )

    def generate_unique_id(self):
        return f"TE{self.department.short_name}{uuid.uuid4().hex[:4].upper()}"

