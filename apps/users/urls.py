from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views.users import UserModelViewSet, TaskModelViewSet, ProjectModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet, 'user')
router.register('task', TaskModelViewSet, 'task')
router.register('project', ProjectModelViewSet, 'project')

urlpatterns = [
    path('', include(router.urls)),
    # path('task-create',TaskApiView.as_view(), name = 'task-create')

]
