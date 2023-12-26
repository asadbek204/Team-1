from django.urls import path
from .views import home, GalleryListView

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', GalleryListView.as_view(), name='gallery')
]