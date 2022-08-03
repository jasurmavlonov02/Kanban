from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views.users import UserModelViewSet, TaskModelViewSet, ProjectModelViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('user', UserModelViewSet, 'user')
router.register('task', TaskModelViewSet, 'task')
router.register('project', ProjectModelViewSet, 'project')


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    # path('task-create',TaskApiView.as_view(), name = 'task-create')
]
