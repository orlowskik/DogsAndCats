from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .models import Pet


# Create your views here.
class IndexView(TemplateView):
    template_name = 'DogsAndCats_content/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        context['kinds'] = Pet.objects.values('kind').distinct()
        context['breeds'] = Pet.objects.values('breed').distinct()
        context['colors'] = Pet.objects.values('color').distinct()
        return context


def get_breeds(request):
    result = request.POST.get('result', None)
    breeds = Pet.objects.filter(kind=result).values('breed').distinct()
    data = {}
    for breed in breeds:
        data[breed["breed"]] = breed["breed"]
    return JsonResponse(data)




