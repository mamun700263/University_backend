from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import University
from .serializers import UniversitySerializer


class UniversityAPIView(APIView):
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(
            universities,
            many=True
        )
        return Response(
            serializer.data
        )

    def post(self, request):
        # print("***********************")
        # print(request.data)
        serializer = UniversitySerializer(
            data=request.data
        )
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UniversityModifyView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            # Retrieve the university by id
            university = University.objects.get(
                id=id
            )
        except University.DoesNotExist:
            return Response(
                {"error": "University not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialize the university data
        serializer = UniversitySerializer(university)
        return Response(
            serializer.dat
        )

    def patch(self, request, id, *args, **kwargs):
        try:
            university = University.objects.get(
                id=id
            )
        except University.DoesNotExist:
            return Response(
                {"error": "University Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Validate and update with the serializer
        serializer = UniversitySerializer(
            university,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
