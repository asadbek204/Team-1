from django.urls import path

from .views.login import *
from .views.generate_password import *
from .views.email import *
from .views.change_password import *
from .views.qaytadan_parolni_yangilash import *
from .views.profile import profile

urlpatterns = [
    path('', login, name='login'),
    path('profile/', profile, name='profile'),
    path('generate_password', generate_password, name='generate_password'),
    path('email', email, name='email'),
    path('change_password', change_password, name='change_password'),
    path('qaytadan_parolni', qaytadan_parolni, name='qaytadan_parolni')
]
