from django.urls import path
from .views import expert_registration

urlpatterns = [
    path("login/", expert_registration.ExpertRegView.as_view(), name="expert_reg")
]
