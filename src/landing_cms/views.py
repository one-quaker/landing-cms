from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['block_list'] = [
            dict(name='hello', content=['hello', 'world']),
            dict(name='projects', content=['Facebook', 'Instagram', 'Telegram']),
            dict(name='team', content=['Bill Gates', 'Elon Musk', 'Linus Torvalds']),
        ]
        return ctx
