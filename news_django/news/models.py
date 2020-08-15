from django.db import models
from django.contrib.auth.models import AbstractUser

from core.model_utils import BaseModel


CATEGORIES = (
    ("nacional", "Nacional"),
    ("regional", "Regional"),
)


class User(AbstractUser, BaseModel):
    # id = models.UUIDField
    # username: models.CharField
    # password: models.PasswordField
    # email: models.EmailField
    # first_name: models.CharField
    # last_name: models.CharField

    # is_active: models.BooleanField
    # is_staff: models.BooleanField
    # is_superuser: models.BooleanField
    # last_login: models.DateTimeField
    # date_joined: models.DateTimeField
    # created: models.DateTimeField
    # updated: models.DateTimeField

    debug_toolbar = models.BooleanField(default=False)

    class Meta:
        verbose_name = "NewsNews User"
        verbose_name_plural = "NewsNews Users"

    def __json__(self, *attrs):
        return self.attrs(
            "id",
            "organization_id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_god",
            "last_login",
            "date_joined",
            "created",
            "updated",
            *attrs,
        )


class NewsItem(BaseModel):
    title = models.TextField(max_length=1024)
    link = models.URLField()
    description = models.TextField(max_length=4096)
    category = models.CharField(
        max_length=128,
        choices=CATEGORIES,
        null=True
    )
    city = models.CharField(max_length=128)
    tags = models.CharField(max_length=1024)
