from django.urls import path
from rest_framework.routers import DefaultRouter

from store import views
#   function base
# urlpatterns = [
#     path('products/', views.product_list),
#     path('products/<int:pk>/', views.product_details)
# ]

router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='products')


# urlpatterns = [
#     path('products/', views.ProductViewSet.as_view()),
#     # path('products/<int:pk>/', views.ProductDetail.as_view())
# ]
urlpatterns = router.urls
