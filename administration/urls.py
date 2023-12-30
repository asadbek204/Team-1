from django.urls import path
from .views import contact, payment


urlpatterns = [
    path('contact/', contact.contact, name='contact'),
    path('payment/', payment.PaymentView.as_view(), name='payment'),
    path('error/', payment.ErrorView.as_view(), name='error')
]
