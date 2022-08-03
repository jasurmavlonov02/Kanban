from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions

from apps.users.models import User, Task, Project
from apps.users.serializers.users import UserModelSerializer, RegisterModelSerializer, TaskModelSerializer, \
    ProjectModelSerializer
from users.permissions import IsAdminRole, IsDeveloperRole
from users.serializers.users import ProjectCreateModelSerializer, ProjectDetailModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_url_kwarg = 'pk'
    permission_classes = (IsAuthenticated,)

    @action(methods=['post'], detail=False, url_path='register', serializer_class=RegisterModelSerializer)
    def user_register(self, request):
        serialized_data = RegisterModelSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        data = {
            'message': 'User successfully created!'
        }
        return Response(data, status.HTTP_201_CREATED)


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    lookup_url_kwarg = 'pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    lookup_url_kwarg = 'pk'

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateModelSerializer
        elif self.action in ['retrieve']:
            return ProjectDetailModelSerializer
        return super().get_serializer_class()

    # permission_classes = (DjangoModelPermissions,)

    def create(self, request, *args, **kwargs):
        print(12334)
        return super().create(request, *args, **kwargs)

