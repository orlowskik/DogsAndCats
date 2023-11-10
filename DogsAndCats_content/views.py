from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
def IndexView(request):
    return render(request, 'DogsAndCats_content/index.html')
