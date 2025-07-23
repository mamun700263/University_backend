from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from ..usermanagers.base_user_manager import CustomUserManager


class UniUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    full_name = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=20, blank=True, null=True,
        validators=[RegexValidator(regex=r'^\+?\d{7,15}$')]
    )
    is_verified = models.BooleanField(default=False)

    class Roles(models.TextChoices):
        STUDENT = "student", "Student"
        TEACHER = "teacher", "Teacher"
        STAFF = "staff", "Staff"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.STUDENT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name} {self.email}"

    def has_role(self, *roles):
        return self.role in roles

    @property
    def is_teacher(self):
        return self.role == self.Roles.TEACHER

    @property
    def is_student(self):
        return self.role == self.Roles.STUDENT

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN

    class Meta:
        swappable = 'AUTH_USER_MODEL'