from django.urls import path
from .views import view_rules


urlpatterns = [
    path('', view_rules)
]
