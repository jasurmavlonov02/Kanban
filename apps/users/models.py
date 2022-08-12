from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, CharField, ForeignKey, TextField, IntegerField, SlugField, CASCADE, IntegerChoices, \
    FileField, PositiveIntegerField, ImageField, EmailField, TextChoices
from django.utils.text import slugify

from apps.shared.models import BaseModel, DeletedModel
from apps.users.managers import UserManager


class User(AbstractUser, BaseModel, DeletedModel):
    class Role(TextChoices):
        ADMIN = 'admin'
        PROJECT_MANAGER = 'project_manager'
        DEVELOPER = 'developer'

    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    username = CharField(max_length=100, unique=True)
    phone_number = CharField(max_length=12)
    photo = ImageField(upload_to='media/')
    email = EmailField(unique=True)
    role = CharField(max_length=15, choices=Role.choices, blank=True, null=True)

    objects = UserManager()


class Project(DeletedModel, BaseModel):
    title = CharField(max_length=225)
    code = CharField(max_length=100)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)


class Task(DeletedModel,BaseModel):
    class Priority(IntegerChoices):
        SMALL = 1
        MEDIUM = 2
        HIGH = 3

    title = CharField(max_length=100)
    text = TextField()
    point = IntegerField(default=0)
    priority = IntegerField(choices=Priority.choices, null=True, blank=True)
    to_user = ForeignKey('users.User', CASCADE, 'tasks')
    author = ForeignKey('users.User', CASCADE, 'author_task')
    step = IntegerField()
    slug = SlugField(unique=True)
    project = ForeignKey('users.Project', CASCADE)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Task.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)


class Comment(DeletedModel, BaseModel):
    message = TextField()
    task = ForeignKey('users.Task', CASCADE, null=True)
    # slug = SlugField(unique=True)
    # FILE =

    # user = ManyToManyField('User')

    # Step:
    # index
    # unique


class File(BaseModel):
    # task = ForeignKey('users.Task', CASCADE, null=True, blank=True)
    # comment = ForeignKey('users.Comment', CASCADE, null=True, blank=True)
    # project = ForeignKey('users.Comment', CASCADE, null=True, blank=True)
    # chapter = ForeignKey('users.Comment', CASCADE, null=True, blank=True)
    # lesson = ForeignKey('users.Comment', CASCADE, null=True, blank=True)

    file = FileField(upload_to='file/')
    content_type = ForeignKey(ContentType, CASCADE)  # 7 yoki 9
    object_id = PositiveIntegerField()  # 2

    content_object = GenericForeignKey()
