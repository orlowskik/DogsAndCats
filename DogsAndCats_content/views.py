from django.shortcuts import render
from django.views.generic import ListView
from .models import Pet


# Create your views here.
class IndexView(ListView):
    template_name = 'DogsAndCats_content/index.html'
    context_object_name = 'dogs_and_cats'

    def get_queryset(self):
        return Pet.objects.all()


