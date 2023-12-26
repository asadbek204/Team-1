from django.urls import path
from .views.login import *
urlpatterns = [
    path('', login, name='login')
]