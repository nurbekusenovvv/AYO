from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', include('apps.mainpage.urls')),
    path('users/', include('apps.users.urls')),
]