from django.contrib import admin

from news.models import User, NewsItem

admin.site.register(User)
admin.site.register(NewsItem)
