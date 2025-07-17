import uuid

from django.contrib.auth.models import User
from .base_user import UniUser
from django.core.validators import RegexValidator
from django.db import models



class Account(models.Model):
    """
    Base Account class for all user accounts.
    """
    user = models.OneToOneField(
        UniUser,
        on_delete=models.CASCADE,
        related_name="account"
        )
    date_of_birth = models.DateField(blank=True, null=True)
    unique_id = models.CharField(
        unique=True,
        max_length=11,
        null=True,
        blank=True
        )
    bio = models.TextField(blank=True, null=True)
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

    def generate_unique_id(self, prefix='', suffix=''):
        return f"{prefix}{uuid.uuid4().hex[:8].upper()}"


def zero_str(count):
    if 10 < count < 100:
        return f'0{count}'
    elif count < 10:
        return f'00{count}'
    else:
        return str(count)

