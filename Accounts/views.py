from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

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
    authentication_classes = []  # Disable default authentication
    permission_classes = [AllowAny]  # Allow access to anyone

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # Debugging: Check validated data
            print("Validated Data:", serializer.validated_data)

            # Authenticate the user
            user = authenticate(username=username, password=password)

            # Debugging: Check authentication result
            if user:
                print("Authenticated User:", user)
                # Create or get the token for the user
                token, created = Token.objects.get_or_create(user=user)
                auth_login(request, user)  # Log the user in
                return Response(
                    {"token": token.key, "user_id": user.id},
                    status=status.HTTP_200_OK
                )
            else:
                print("Authentication failed for user:", username)
                return Response(
                    {"error": "Invalid username or password"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            # Debugging: Log serializer errors
            print("Serializer Errors:", serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
