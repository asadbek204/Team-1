from django.urls import path
from .views import contact

urlpatterns = [
    path('contact/', contact.contact, name='contact')
]
