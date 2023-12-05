from django.urls import path

from store import views
#   function base
# urlpatterns = [
#     path('products/', views.product_list),
#     path('products/<int:pk>/', views.product_details)
# ]


urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetails.as_view())
]