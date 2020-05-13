from django.contrib import admin
from django.urls import path
from django.urls import include
from myblog.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gideon/', include('gideon.urls')),
    path('annunziata/', include('annunziata.urls')),
    path('', index),
]
