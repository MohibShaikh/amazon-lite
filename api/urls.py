from django.urls import path
from .serializers import ProductInfoSerializer
from .views import *

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('products/<int:pk>', get_product, name='get_product'),
    path('delete/<int:pk>', DeleteProductAPIView.as_view(), name='delete_product'),
    path('detail/<int:pk>', ProductDetailAPIView.as_view(), name='product_detail'),
    path('orders/', order_list, name='order_list'),
    path('products/create/', CreateProductAPIView.as_view(), name='create_product'),
    path('orders/<uuid:pk>', delete_order, name='delete_order'),
    path('products/info/', get_prod_info, name='get_prod_info'),
]
