from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Pet


# Create your views here.
class IndexView(TemplateView):
    template_name = 'DogsAndCats_content/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        context['kinds'] = Pet.objects.values('kind').distinct()
        return context




