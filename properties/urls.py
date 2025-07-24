from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← HOME PAGE
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('developers/', views.developer_list, name='developer_list'),
    path('subdivision/<int:subdiv_id>/', views.subdivision_properties, name='subdivision_properties'),
]
