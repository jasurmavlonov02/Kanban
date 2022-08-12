from rest_framework.viewsets import ModelViewSet
from apps.users.models import Project
from apps.users.serializers.projects import ProjectModelSerializer, ProjectCreateModelSerializer, \
    ProjectDetailModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    lookup_url_kwarg = 'pk'

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateModelSerializer
        elif self.action in ['retrieve',]:
            return ProjectDetailModelSerializer
        return super().get_serializer_class()

    # permission_classes = (DjangoModelPermissions,)
