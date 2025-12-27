from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path('', views.equipment_list, name='list'),
    path('add/', views.add_equipment, name='add'),
    path('<int:pk>/', views.equipment_detail, name='detail'),
]
