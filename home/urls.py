from django.urls import path
from .views import home, gallery

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery')
]