from django.contrib import admin

# Register your models here.
from users.models import Task, Project, Comment, File


admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(File)