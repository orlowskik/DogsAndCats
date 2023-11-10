from django.urls import path
from DogsAndCats_content.views import IndexView


urlpatterns = [
    path('', IndexView),
]
