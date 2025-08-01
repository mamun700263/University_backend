# Generated by Django 5.2 on 2025-07-23 00:11

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Departments", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("batch", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "unique_id",
                    models.CharField(blank=True, max_length=11, null=True, unique=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "mobile",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Mobile number must be exactly 11 digits.",
                                regex="^\\d{11}$",
                            )
                        ],
                    ),
                ),
                (
                    "profile_picture",
                    models.URLField(
                        blank=True,
                        default="https://i.imgur.com/placeholder.png",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuthorityAccount",
            fields=[
                (
                    "account_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Accounts.account",
                    ),
                ),
            ],
            bases=("Accounts.account",),
        ),
        migrations.CreateModel(
            name="StaffAccount",
            fields=[
                (
                    "account_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Accounts.account",
                    ),
                ),
            ],
            bases=("Accounts.account",),
        ),
        migrations.CreateModel(
            name="UniUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\+?\\d{7,15}$"
                            )
                        ],
                    ),
                ),
                ("is_verified", models.BooleanField(default=False)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("student", "Student"),
                            ("teacher", "Teacher"),
                            ("staff", "Staff"),
                            ("admin", "Admin"),
                        ],
                        default="student",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "swappable": "AUTH_USER_MODEL",
            },
        ),
        migrations.AddField(
            model_name="account",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="account",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="StudentAccount",
            fields=[
                (
                    "account_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Accounts.account",
                    ),
                ),
                ("Class_Representetive", models.BooleanField(default=False)),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="batch.batch",
                        verbose_name="Batch",
                    ),
                ),
            ],
            bases=("Accounts.account", models.Model),
        ),
        migrations.CreateModel(
            name="TeacherAccount",
            fields=[
                (
                    "account_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Accounts.account",
                    ),
                ),
                ("Department_head", models.BooleanField(default=False)),
                (
                    "department",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Departments.department",
                        verbose_name="Department",
                    ),
                ),
            ],
            bases=("Accounts.account", models.Model),
        ),
    ]
