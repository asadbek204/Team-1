from django.urls import path
from .views import *


urlpatterns = [
    path('', contact_view, name='contact'),
    path('profile', profile_view, name='profile'),
    path('forgot_password', password_reset_view,name='forgot_password')
]