from django.db import models

from core.model_utils import BaseModel


CATEGORIES = (
    ("nacional", "Nacional"),
    ("regional", "Regional"),
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
