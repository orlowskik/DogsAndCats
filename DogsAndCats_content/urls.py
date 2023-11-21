from django.template.defaulttags import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'get_breeds', views.get_breeds, name='get_breeds'),
]
