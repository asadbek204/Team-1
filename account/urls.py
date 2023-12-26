from django.urls import path
from .views.login import *
from .views.profile import profile

urlpatterns = [
    path('', login, name='login'),
    path('profile/', profile, name='profile')
]