from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from celery.result import AsyncResult
from .models import Image
from .serializers import ImageSerializer
from .tasks import process_image_task  # Celery task


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # используем get_serializer()
        serializer.is_valid(raise_exception=True)
        image_instance = serializer.save()
        # Запускаем фоновую задачу Celery
        task = process_image_task.delay(image_instance.id)
        response_data = serializer.data
        response_data['task_id'] = task.id  # возвращаем ID задачи для клиента
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='task-status/(?P<task_id>[^/.]+)')
    def task_status(self, request, task_id=None):
        result = AsyncResult(task_id)
        # Обработка случая отсутствия результата или backend отключён
        status_value = result.status if result else 'UNKNOWN'
        data = {
            'task_id': task_id,
            'status': status_value,
            'result': result.result if result.ready() else None,
        }
        return Response(data)
