from django.urls import path
from .views.login import LoginView
from .views.profile import ProfileView
from .views.registration import register_view
from .views.forgot_password import ForgotPasswordView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', register_view, name='registration'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password')
]
