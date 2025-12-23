from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>', views.update_product, name='update_product'),
    path('delete/<str:name>', views.delete_product, name='delete_product'),
    # path('<str:name>/update', views.update_product, name='update_product'),
]
