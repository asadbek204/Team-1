from django.urls import path
from .views import expert_registration

urlpatterns = [
<<<<<<< HEAD
    path("login/", expert_registration.ExpertRegView.as_view(), name="expert_reg")
]
=======
    path("", expert_registration.ExpertRegView.as_view(), name="expert_reg")

]
>>>>>>> 74ef68f (fixing config:urls.py)
