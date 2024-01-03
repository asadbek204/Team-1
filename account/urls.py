from django.urls import path
from .views.login import *
from .views.profile import ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('login/', login, name='login'),
]
