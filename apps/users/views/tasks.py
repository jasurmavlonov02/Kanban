from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.users.models import Task
from apps.users.serializers.tasks import TaskModelSerializer, TaskCreateSerializer, TaskDetailSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    lookup_url_kwarg = 'pk'
    filterset_fields = ['title', 'create_at']

    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        elif self.action in ['retrieve', ]:
            return TaskDetailSerializer
        return super().get_serializer_class()
