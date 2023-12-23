from django.urls import path
from main.views import create_expert_view

urlpatterns = [
    path('', create_expert_view, name='create_expert'),
]
