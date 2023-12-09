from django.urls import path
from .views import results_view

urlpatterns = [
    path("results/", results_view, name="results" )
]