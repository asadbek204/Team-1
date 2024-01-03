from django.urls import path
from .views.login import login
from .views.profile import ProfileView
from .views.registration import register_view

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('login/', login, name='login'),
    path('registration/', register_view, name='registration')
]
