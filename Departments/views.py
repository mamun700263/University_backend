
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Batch, Department
from .serializers import BatchSerializer, DepartmentSerializer


class DepartmentAPIView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentModifyView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            # Retrieve the Department by id
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response(
                {"error": "Department not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialize the Department data
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def patch(self, request, id, *args, **kwargs):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response(
                {"error": "Department Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Validate and update with the serializer
        serializer = DepartmentSerializer(
            department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BatchAPIView(APIView):
    def get(self, request):
        batchs = Batch.objects.all()
        serializer = BatchSerializer(batchs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BatchModifyView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            # Retrieve the Batch by id
            batch = Batch.objects.get(id=id)
        except Batch.DoesNotExist:
            return Response(
                {"error": "Batch not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Serialize the Batch data
        serializer = BatchSerializer(batch)
        return Response(serializer.data)

    def patch(self, request, id, *args, **kwargs):
        try:
            batch = Batch.objects.get(id=id)
        except Batch.DoesNotExist:
            return Response(
                {"error": "Batch Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Validate and update with the serializer
        serializer = BatchSerializer(batch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
