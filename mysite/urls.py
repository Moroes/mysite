from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest.views import PostAPIView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path("", include("main.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/postlist/', PostAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

