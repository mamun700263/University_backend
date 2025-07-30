import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Batch
from .serializers import BatchSerializer

logger = logging.getLogger("batch.model")


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.info(f"✅ Batch created: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"❌ Batch creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.get_object()
        except Batch.DoesNotExist:
            logger.error(f"❌ Batch not found for update: ID {pk}")
            return Response({"error": "Batch not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            logger.info(f"🔄 Batch updated: ID {pk}")
            return Response(serializer.data)
        logger.warning(f"❌ Invalid data on update for Batch ID {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
