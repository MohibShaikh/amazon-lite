from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status  # For proper HTTP status codes
from django.shortcuts import get_object_or_404 # Prevents crashes
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request, pk):
    # get_object_or_404 returns 404 instead of crashing the server
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    # Return errors so your Vue frontend knows WHY it failed
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete_product(request, name):
    product = get_object_or_404(Product, name=name)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)