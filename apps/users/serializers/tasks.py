from datetime import datetime

from rest_framework.serializers import ModelSerializer

from apps.users.models import Task


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('is_deleted', 'deleted_at', 'update_at')


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ('is_deleted', 'deleted_at', 'update_at')


class TaskDetailSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ()

    def to_representation(self, instance):
        result = super().to_representation(instance)
        datetime_data = datetime.strptime(result['create_at'], '%Y-%m-%d %H:%M:%S')
        if datetime_data.year < 2021:
            datetime_data = datetime_data.replace(year=2020)
            result['create_at'] = datetime_data.strftime('%Y-%m-%d %H:%M:%S')
        return result
