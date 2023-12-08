from django.urls import path
from .views import *


urlpatterns = [
    path('', contact_view, name='contact')
]