from django.urls import path
from .views.login import *
from .views.profile import profile

urlpatterns = [
    path('', profile, name='profile'),
    path('login/', login, name='login'),
]
