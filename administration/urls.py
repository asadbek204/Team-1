from django.urls import path
from .views import contact, payment, rules
from .views.create_expert import *


urlpatterns = [
    path('contact/', contact.contact, name='contact'),
    path('payment/', payment.PaymentView.as_view(), name='payment'),
    path('error/', payment.ErrorView.as_view(), name='error'),
    path('create_expert/', create_expert, name='create_expert'),
    path('rules/', rules.rules, name='rules')
]
