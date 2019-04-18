from django.views.generic import TemplateView, ListView

from .models import Block


class IndexView(ListView):
    template_name = 'index.html'
    model = Block
    context_object_name = 'block_list'
    queryset = Block.objects.all().prefetch_related('skill_list', 'team_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
