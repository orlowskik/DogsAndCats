from django.template.defaulttags import url
from django.urls import path, re_path

from . import views

app_name = 'DogsAndCats_content'
urlpatterns = [
    path("<kind>/<breed>/<color>/", views.IndexView.as_view(), name='index'),
    path("", views.IndexView.as_view(), name='blind_index'),
    path(r'get_breeds', views.get_breeds, name='get_breeds'),
    path(r'get_colors', views.get_colors, name='get_colors'),
    path(r'search/', views.search, name='search'),
]
