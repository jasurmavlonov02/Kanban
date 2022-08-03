from django.contrib import admin
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.auth.admin import UserAdmin

from apps.users.models import Task, Project, Comment, File, User

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)


# admin.site.register(File)


class CommentFileProxy(File):
    class Meta:
        verbose_name = 'Commentga tegishli fayllar'
        verbose_name_plural = 'Commentga tegishli fayllar'
        proxy = True


class TaskFileProxy(File):
    class Meta:
        verbose_name = 'Taskka tegishli fayllar'
        verbose_name_plural = 'Taskka tegishli fayllar'
        proxy = True


class FileMixin:
    list_display = ('file', 'object_id', 'content_type')


@admin.register(File)
class FileAdmin(FileMixin, admin.ModelAdmin):
    pass


@admin.register(TaskFileProxy)
class TaskFileProxyAdmin(FileMixin, admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # return File.objects.filter(content_type=get_content_type_for_model(Task))
        return queryset.filter(content_type=get_content_type_for_model(Task))


@admin.register(CommentFileProxy)
class CommentFileProxyAdmin(FileMixin, admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(content_type=get_content_type_for_model(Comment))


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Addition fields"), {"fields": ("phone_number", "photo")}),
    )

# admin.site.register(User, CustomUserAdmin)
