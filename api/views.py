from urllib import request

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max, Sum, F
from rest_framework import status, generics  # For proper HTTP status codes
from django.shortcuts import get_object_or_404  # Prevents crashes
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['PUT'])
def update_product(request, pk):
    # get_object_or_404 returns 404 instead of crashing the server
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.prefetch_related('items__product').annotate(
        total_price=Sum(F('items__quantity') * F('items__product__price'))
    )

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_prod_info(request):
    products = Product.objects.all()
    json_data = ProductInfoSerializer({'products': products,
                                       'count': len(products),
                                       'max_price': products.aggregate(max_price=Max('price'))['max_price']
                                       }
                                      )

    return Response(json_data.data, status=status.HTTP_200_OK)
