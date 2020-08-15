from core.view_utils import BaseView


class Home(BaseView):
    template = "news/home.html"

    def get(self, request, *args, **kwargs):
        return self.render_template(request)
