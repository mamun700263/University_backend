import logging

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger("account.views")

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    Account,
    AuthorityAccount,
    StaffAccount,
    StudentAccount,
    TeacherAccount,
)
from .serializers import (
    AccountSerializer,
    AuthorityAccountSerializer,
    LoginSerializer,
    StaffAccountSerializer,
    StudentAccountSerializer,
    TeacherAccountSerializer,
)


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
    permission_classes = [AllowAny]

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        tokens = self.get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)

            token.blacklist()
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response(
                {"error": "Invalid or missing refresh token"},
                status=status.HTTP_400_BAD_REQUEST,
            )
