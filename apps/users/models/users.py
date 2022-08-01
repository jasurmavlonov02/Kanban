from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Model, DateTimeField, BooleanField, CharField, ForeignKey, TextField, EmailField, \
    PositiveIntegerField, IntegerField, ImageField, ManyToManyField, CASCADE, IntegerChoices , FileField

from apps.shared.models import BaseModel, DeletedModel





class Project(DeletedModel , BaseModel):
    title = CharField(max_length=225)
    code = CharField(max_length=100, default=f'{title}-{len(title)}')


class Task(Model):

    class Priority(IntegerChoices):
        SMALL = 'SMALL'
        MEDIUM = 'MEDIUM'
        LARGE = 'LARGE'

    class Status(IntegerChoices):
        pass

    title = CharField(max_length=100)
    text = TextField()
    point = CharField(max_length=100)
    to_user = ForeignKey('User', CASCADE , 'user')
    priority = IntegerField(choices=Priority.choices, null=True, blank=True)
    status = IntegerField(choices=Status.choices, null=True, blank=True)
    author = ForeignKey('User' , CASCADE , null=True)
    step = IntegerField()
    project = ForeignKey('Project' , CASCADE)


class Comment(DeletedModel , BaseModel):
    message = TextField()
    file = FileField(upload_to='comment-media/')
    task_fk = ForeignKey('Task' , CASCADE , null=True)
    # FILE =

    comment_fk = ManyToManyField('User', CASCADE)
    # Step:
    # index
    # unique

    class UserManager(BaseUserManager):

        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('User should have phone number ! ')
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, email, password=None, **extra_fields):
            user = self.create_user(email, password, **extra_fields)
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user

    class User(AbstractUser, BaseModel, DeletedModel):
        class Role(IntegerChoices):
            ADMIN = 'ADMIN'
            PROJECT_MANAGER = 'PROJECT_MANAGER'
            DEVELOPER = 'DEVELOPER'

        first_name = CharField(max_length=20)
        last_name = CharField(max_length=20)
        username = CharField(max_length=100)
        phone_number = CharField(max_length=12)
        photo = ImageField(upload_to='media/')
        email = EmailField()
        role = ManyToManyField(choices=Role.choices, null=True, blank=True)
        objects = UserManager()




