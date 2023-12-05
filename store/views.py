from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.decorators import api_view
from .serializers import  ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Product
# Create your views here.


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data )


@api_view()
def product_details(resquest, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return HttpRequest(serializer.data)