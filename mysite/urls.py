from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('evrekabackend/', include('evrekabackend.urls')),
    path('admin/', admin.site.urls),
]