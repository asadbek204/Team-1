from django.urls import path
from .views import view_registration


urlpatterns = [
    path('', view_registration)
]
