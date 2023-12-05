from django.http import JsonResponse
from django.shortcuts import reverse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Pet


# Create your views here.

class IndexView(TemplateView):
    template_name = 'DogsAndCats_content/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pets'] = self.get_data(kwargs)
        context['kinds'] = Pet.objects.values('kind').distinct()
        return context

    def get_data(self, kwargs):
        context = Pet.objects.all()
        print('render')
        print(kwargs)
        try:
            pets = Pet.objects.all().values('kind').distinct()
            kinds = [kind['kind'] for kind in pets]
            if kwargs['kind'] in kinds:
                context = Pet.objects.filter(kind=kwargs['kind'])
                breeds = [breed['breed'] for breed in context.values("breed").distinct()]
                colors = [color['colors'] for color in context.values('color').distinct()]
                try:
                    if kwargs['breed'] in breeds:
                        context = context.filter(breed__in=kwargs['breed'])
                        print(context)
                except KeyError:
                    print('Bad value for breed')
                try:
                    if kwargs['color'] in colors:
                        context = context.filter(color__in=kwargs['color'])
                except KeyError:
                    print('Bad value for color')
        except KeyError:
            context = Pet.objects.all()
        print(context)
        return context


def get_breeds(request):
    result = request.POST.get('result', None)
    breeds = Pet.objects.filter(kind=result).values('breed').distinct()
    data = {}
    for breed in breeds:
        data[breed["breed"]] = breed["breed"]
    return JsonResponse(data)


def get_colors(request):
    result = request.POST.get('result', None)
    colors = Pet.objects.filter(kind=result).values('color').distinct()
    data = {}
    for color in colors:
        data[color["color"]] = color["color"]
    return JsonResponse(data)


def search(request):
    kind = request.POST.get('kind')
    breed = request.POST.get('breed')
    colors = request.POST.get('colors')
    print(kind, breed, colors)
    return HttpResponseRedirect(reverse('DogsAndCats_content:index', args=(kind, breed, colors,)))
