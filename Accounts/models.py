import uuid

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# from Departments.models import Batch


class Account(models.Model):
    """
    Base Account class for all user accounts.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="account"
        )
    date_of_birth = models.DateField(
        blank=True,
        null=True
        )
    unique_id = models.CharField(
        unique=True,
        max_length=11,
        null=True,
        blank=True
        )
    bio = models.TextField(
        blank=True,
        null=True
        )
    mobile = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="Mobile number must be exactly 11 digits.",
            )
        ],
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        default="https://i.imgur.com/placeholder.png",
        # Replace with a valid placeholder URL
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self, prefix, suffix):
        return f"{prefix}{uuid.uuid4().hex[:8].upper()}"


class StudentAccount(Account):
    """
    Student account with a unique ID format.
    """

    Class_Representetive = models.BooleanField(
        default=False
        )
    batch = models.ForeignKey(
        "Departments.Batch",
        verbose_name="Batch",
        on_delete=models.CASCADE
    )

    def generate_unique_id(self):
        self.batch.total_students += 1
        self.batch.save()
        return Account.generate_unique_id(
            self,
            'ST',
            str(self.batch.total_students)
            )


class TeacherAccount(Account):
    """
    Teacher account with a unique ID format.
    """

    Department_head = models.BooleanField(default=False)

    def generate_unique_id(self):
        return f"TE-{uuid.uuid4().hex[:8].upper()}"


class StaffAccount(Account):
    """
    Staff account with a unique ID format.
    """

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Check if the student is new
        super().save(*args, **kwargs)  # Save the student first
        if is_new:  # Increment count only for new students
            self.batch.student_count += 1
            self.batch.save()

    def generate_unique_id(self):
        return f"OF-{uuid.uuid4().hex[:8].upper()}"


class AuthorityAccount(Account):
    """
    Authority account with a unique ID format.
    """

    def generate_unique_id(self):
        return f"AU-{uuid.uuid4().hex[:8].upper()}"
