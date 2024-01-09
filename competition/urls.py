from django.urls import path
from .views import competition_view, questionare, detail


urlpatterns = [
    path('', competition_view, name='competition'),
    path('questionare/', questionare, name='questionare'),
    path('detail/', detail, name='detail')
]
