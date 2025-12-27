from django.contrib import admin
from django.urls import path, include
from .views import home_view, health_view, calendar_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('equipment/', include('equipment.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('notifications/', include('notifications.urls')),
    path('calendar/', calendar_view, name='calendar'),
    path('', home_view, name='home'),
    path('health/', health_view, name='health'),
]
