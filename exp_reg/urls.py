from django.urls import path
from .views import exp_reg_view

urlpatterns = [
    path("", exp_reg_view, name="exp_reg")
]