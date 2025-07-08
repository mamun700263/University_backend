import uuid
from .base_account import Account

from django.db import models


class StudentAccount(Account,models.Model):
    """
    Student account with a unique ID format.
    """
    Class_Representetive = models.BooleanField(default=False)
    batch = models.ForeignKey(
        "batch.Batch",
        verbose_name="Batch",
        on_delete=models.CASCADE
    )

    def generate_unique_id(self):
        self.batch.total_students += 1
        self.batch.save()
        count = Account.zero_str(self.batch.total_students)
        batch_name = self.batch.short_name
        id = f'ST{batch_name}{count}'
        return id

