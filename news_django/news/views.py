from core.view_utils import BaseView
from news.models import NewsItem


class Home(BaseView):
    template = "news/home.html"

    def get(self, request, *args, **kwargs):
        context = {"news_items": NewsItem.objects.all()}
        return self.render_template(request, context)
