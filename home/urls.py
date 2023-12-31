from django.urls import path
from .views import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery')
]
