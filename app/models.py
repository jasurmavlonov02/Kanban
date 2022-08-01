from django.contrib.auth.models import AbstractUser
from django.db.models import Model, DateTimeField, BooleanField, CharField, ForeignKey, TextField, EmailField, \
    PositiveIntegerField, IntegerField, ImageField, ManyToManyField, CASCADE, IntegerChoices , FileField


class BaseModel(Model):
    create_at = DateTimeField(auto_now=True)
    update_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DeletedModel(Model):
    deleted_at = DateTimeField(null=True, blank=True)
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True

class Role(Model):
    'CEO'
    'Branch'
    'Director'
    'Administrator'
    'Administrator'
    name = CharField(max_length=255)


class User(AbstractUser , BaseModel ,DeletedModel ):

    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    username = CharField(max_length=100)
    phone_number = CharField(max_length=12)
    photo = ImageField(upload_to='media/')
    email = EmailField()
    role =ManyToManyField('Role' , related_name='role')



class Project(DeletedModel , BaseModel):
    title = CharField(max_length=225)
    code = CharField(max_length=100, default=f'{title}-{len(title)}')


class Task(Model):

    class Priority(IntegerChoices):
        easy = 'easy'

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


class Comment(DeletedModel , BaseModel):
    message = TextField()
    file = FileField(upload_to='media/')
    task_fk = ForeignKey('Task' , CASCADE , null=True)
    # FILE =

    # comment_fornkey
    # Step:
    # index
    # unique


