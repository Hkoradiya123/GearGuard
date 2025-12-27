from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.maintenance_list, name='list'),
    path('add/', views.add_maintenance_record, name='add'),
    path('<int:pk>/', views.maintenance_detail, name='detail'),
    path('update-status/', views.update_maintenance_status, name='update_status'),
]
