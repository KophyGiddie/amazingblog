from django.contrib import admin
from django.urls import path
from django.urls import include
from myblog.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gideon/', include('gideon.urls')),
    path('lucky/', include('lucky.urls')),
    path('', index),
]
