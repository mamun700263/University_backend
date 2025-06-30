import logging
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
logger = logging.getLogger("account.views")

from .models import (
    Account,
    AuthorityAccount,
    StaffAccount, 
    StudentAccount,
    TeacherAccount
    )
from .serializers import (
    AccountSerializer,
    AuthorityAccountSerializer,
    LoginSerializer,
    StaffAccountSerializer,
    StudentAccountSerializer,
    TeacherAccountSerializer
    )



# Account ViewSets
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

class UserLoginApiView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            logger.debug(f"Attempt login with username: {username}")

            # user = authenticate(request, username=username, password=password)
            user = authenticate(request, email=username, password=password)

            if user:
                logger.info(f"Authenticated User: {user}")
                token, created = Token.objects.get_or_create(user=user)
                auth_login(request, user)
                return Response(
                    {"token": token.key, "user_id": user.id},
                    status=status.HTTP_200_OK
                )
            else:
                logger.debug(f"Authentication failed for user: {username}")
                return Response(
                    {"error": "Invalid username or password"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            logger.error(f"Login Serializer Errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
