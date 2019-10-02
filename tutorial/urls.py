from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'', include('quickstart.urls')),
    path(r'admin/', admin.site.urls),
]