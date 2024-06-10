from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', core_views.signup_view, name='signup'),
    path('login/', core_views.login_view, name='login'),
    path('profile/', core_views.profile_view, name='profile'),
]
