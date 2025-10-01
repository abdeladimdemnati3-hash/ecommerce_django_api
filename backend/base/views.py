from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
        ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    return Response(products)
    
@api_view(['GET'])
def getProduct(request, id):
    product = next((item for item in products if item["_id"] == id), None)
    if product:
        return Response(product)
    else:
        return Response({'message': 'Product not found'}, status=404)        
