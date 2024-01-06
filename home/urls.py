from django.urls import path
from .views import views, search, certificate

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('search/', search.SearchView.as_view(), name='search'),
    path('certificate/', certificate.certificateview, name='certificate')
]
