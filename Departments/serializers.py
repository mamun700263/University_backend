from Accounts.models import StudentAccount
from rest_framework import serializers

from .models import Batch, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

    def student_count(self):
        students = StudentAccount.objects.get( batch=self.model).count()
