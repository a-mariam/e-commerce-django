from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import  ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Product

# Create your views here.
# function base
# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
#
#
# @api_view(['GET', 'POST', 'PATCH', 'DELETE'])
# def product_details(resquest, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if resquest.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#     elif resquest.method == 'PUT':
#         serializer = ProductSerializer(product,data=resquest.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer)
#     elif resquest.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Using oop concept which
# using class base view
# class ProductList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(status=status.HTTP_200_OK,data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data= serializer.data)


# class ProductDetails(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# using generic that means extending a clas
#  class ProductList(ListCreateAPIView):
#      def get_queryset(self):
#          return Product.objects.all()
#
#      def get_serializer_class(self):
#          return  ProductSerializer
#
#
# class ProductDetail(RetrieveUpdateDestroyAPIView):
#      def get_queryset(self):
#          return Product.objects.all()
#

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

