from django.urls import path
from . import views

urlpatterns = [
    path('cinema/', views.index, name='cinema_home'),  # Головна сторінка
    path('cinema/<str:table_name>/', views.dashboard, name='view_table'),
    path('cinema/<str:table_name>/add/', views.add_record, name='add_record'),
    path('cinema/<str:table_name>/edit/<int:pk>/', views.edit_record, name='edit_record'),
    path('cinema/<str:table_name>/delete/<int:pk>/', views.delete_record, name='delete_record'),
]
