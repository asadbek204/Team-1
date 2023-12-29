from django.urls import path
from .views.contact import contact

urlpatterns = [
    path('', contact, name='contact')
]