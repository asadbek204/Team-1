from django.urls import path
from .views import competition_view


urlpatterns = [
    path('', competition_view)
]
