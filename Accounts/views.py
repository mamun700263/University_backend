from rest_framework.viewsets import ModelViewSet

from .models import (Account, AuthorityAccount, StaffAccount, StudentAccount,
                     TeacherAccount)
from .serializers import (AccountSerializer, AuthorityAccountSerializer,
                          StaffAccountSerializer, StudentAccountSerializer,
                          TeacherAccountSerializer)


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class StudentAccountViewSet(ModelViewSet):
    queryset = StudentAccount.objects.all()
    serializer_class = StudentAccountSerializer


class TeacherAccountViewSet(ModelViewSet):
    queryset = TeacherAccount.objects.all()
    serializer_class = TeacherAccountSerializer


class StaffAccountViewSet(ModelViewSet):
    queryset = StaffAccount.objects.all()
    serializer_class = StaffAccountSerializer


class AuthorityAccountViewSet(ModelViewSet):
    queryset = AuthorityAccount.objects.all()
    serializer_class = AuthorityAccountSerializer
