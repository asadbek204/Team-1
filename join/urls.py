from django.urls import path
from .views import joins

urlpatterns = [
    path('join/', joins, name='join')
]