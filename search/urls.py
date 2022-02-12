

from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path("", views.search, name='search_view'),
    path('api/', include('search.api.urls')),
]
