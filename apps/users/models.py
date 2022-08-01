from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, CharField, ForeignKey, TextField, IntegerField, SlugField, CASCADE, IntegerChoices, \
    FileField, PositiveIntegerField

from shared.models import BaseModel, DeletedModel


# class UserManager(BaseUserManager):
#
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('User should have phone number ! ')
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         user = self.create_user(email, password, **extra_fields)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
# class User(AbstractUser, BaseModel, DeletedModel):
#     class Role(IntegerChoices):
#         ADMIN = 1
#         PROJECT_MANAGER = 2
#         DEVELOPER = 3
#
#     first_name = CharField(max_length=20)
#     last_name = CharField(max_length=20)
#     # username = CharField(max_length=100)
#     phone_number = CharField(max_length=12)
#     photo = ImageField(upload_to='media/')
#     # email = EmailField()
#     # role = ManyToManyField(choices=Role.choices, blank=True)
#
#     objects = UserManager()


class Project(DeletedModel, BaseModel):
    title = CharField(max_length=225)
    code = CharField(max_length=100)
    slug = SlugField(unique=True)


class Task(Model):
    class Priority(IntegerChoices):
        SMALL = 1
        MEDIUM = 2
        LARGE = 3

    title = CharField(max_length=100)
    text = TextField()
    point = IntegerField(default=0)
    priority = IntegerField(choices=Priority.choices, null=True, blank=True)
    to_user = ForeignKey('auth.User', CASCADE, 'tasks')
    author = ForeignKey('auth.User', CASCADE, 'author_task')
    step = IntegerField()
    slug = SlugField(unique=True)
    project = ForeignKey('Project', CASCADE)


class Comment(DeletedModel, BaseModel):
    message = TextField()
    task = ForeignKey('Task', CASCADE, null=True)
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

    content_type = ForeignKey(ContentType, CASCADE) # 7 yoki 9
    object_id = PositiveIntegerField() # 2

    content_object = GenericForeignKey()

