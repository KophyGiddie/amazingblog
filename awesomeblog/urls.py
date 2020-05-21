from django.contrib import admin
from django.urls import path
from django.urls import include
from awesomeblog.views import index
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('X123/', admin.site.urls),
    path('nii/', include('Niicode.urls')),
    path('gideon/', include('gideon.urls')),
    path('Nathaniel/', include('Nathaniel.urls')),
    path('annunziata/', include('annunziata.urls')),
    path('lucky/', include('lucky.urls')),
    path('bright/', include('bright.urls')),
    path('users/', include('users.urls')),
    path('', index),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
