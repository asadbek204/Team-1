from django.urls import path
from .views import profile_2_view


urlpatterns = [
    path('', profile_2_view)
]
