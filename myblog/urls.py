from django.contrib import admin
from django.urls import path
from django.urls import include
from myblog.views import index
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gideon/', include('gideon.urls')),
    path('annunziata/', include('annunziata.urls')),
    path('lucky/', include('lucky.urls')),
    path('', index),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]