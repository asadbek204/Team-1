from django.urls import path
from .views import competition_view, questionare


urlpatterns = [
    path('', competition_view),
    path('questionare/', questionare, name='questionare')
]
