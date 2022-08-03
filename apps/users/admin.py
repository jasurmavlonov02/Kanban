from django.contrib import admin

# Register your models here.
from apps.users.models import Task, Project, Comment, File, User

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(File)
admin.site.register(User)
