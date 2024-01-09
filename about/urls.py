from django.urls import path
from .views import about_us, region, result

urlpatterns = [
    path('', about_us.about_view, name='experts'),
    path('result/', result.results_view, name='result'),
    path('region/', region.region_view, name='region')
]
