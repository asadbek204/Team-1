from django.urls import path
from .views import GalleryListView

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery')
]
