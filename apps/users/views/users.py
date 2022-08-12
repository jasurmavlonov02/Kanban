from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions

from apps.users.models import User, Task, Project
from apps.users.serializers.projects import ProjectModelSerializer, ProjectCreateModelSerializer, \
    ProjectDetailModelSerializer
from apps.users.serializers.tasks import TaskModelSerializer
from apps.users.serializers.users import UserModelSerializer, RegisterModelSerializer

from apps.users.permissions import IsAdminRole, IsDeveloperRole


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
