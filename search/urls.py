

from django.urls import path, include
from . import views

app_name = 'search'

urlpatterns = [
    path('api/', include('search.api.urls')),
]
