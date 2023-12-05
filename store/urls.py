from django.urls import path

from store import views

urlPatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_details)
]