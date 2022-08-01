from django.db.models import Model, DateTimeField, BooleanField


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

