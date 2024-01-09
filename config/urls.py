from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    # path('about/', include('about.urls')),
    # path('site/', include('administration.urls')),
    # path('account/', include('user_account.urls')),
    # path('competition/', include('competition.urls')),
    # path('expert/', include('expert.urls')),
    # path('accounts/', include('allauth.urls')),
]
urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('about/', include('about.urls'), name='about'),
    path('site/', include('administration.urls')),
    path('account/', include('user_account.urls')),
    path('competition/', include('competition.urls')),
    path('expert/', include('expert.urls')),
    path('accounts/', include('allauth.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
