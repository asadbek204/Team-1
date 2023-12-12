from django.urls import path
<<<<<<< HEAD
from .views import GalleryListView

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery')
=======
from .views import gallery

urlpatterns = [
    path('', gallery, name='gallery')
>>>>>>> c9565aa (gallery almost done media left)
]