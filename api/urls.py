from django.urls import path
from . import views
from .serializers import ProductInfoSerializer

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>', views.get_product, name='get_product'),
    path('delete/<int:pk>', views.delete_product, name='delete_product'),
    # path('<str:name>/update', views.update_product, name='update_product'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<uuid:pk>', views.delete_order, name='delete_order'),
    path('products/info/', views.get_prod_info, name='get_prod_info'),
]
