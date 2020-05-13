from django.contrib import admin
from django.urls import path
from django.urls import include
from myblog.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nii/', include('Niicode.urls')),
    path('gideon/', include('gideon.urls')),
    path('Nathaniel/', include('Nathaniel.urls')),
    path('annunziata/', include('annunziata.urls')),
    path('lucky/', include('lucky.urls')),
    path('bright/', include('bright.urls')),
    path('', index),
]
