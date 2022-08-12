from rest_framework.serializers import ModelSerializer
from apps.users.models import Project


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        # fields = '__all__'
        exclude = ('is_deleted', 'deleted_at', 'update_at')


class ProjectCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'code')


class ProjectDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
