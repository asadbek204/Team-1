from django.urls import path
from .views import expert_registration, matching


urlpatterns = [
    path('', matching.expert_matching, name='matching'),
    path("login/", expert_registration.ExpertRegView.as_view(), name="expert_reg")
]
