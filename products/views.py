from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Category, Product
from .serializers import (
    CategoryListSerializer,
    ProductListSerializer,
    ProductDetailSerializer
)
# Create your views here.
class CategoryListApi(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer   
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        slug = serializer.validated_data.get('slug')
        if slug is None:
            slug = name
        serializer.save(slug=slug) 
        
    


class ProductListApi(ModelViewSet):
    queryset = Product.objects.prefetch_related('category').all()
    serializer_class = ProductDetailSerializer
    
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        price = serializer.validated_data.get('price')
        serializer.save(seller=self.request.user)
    
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return ProductListSerializer
        return super().get_serializer_class()
    
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        seller = request.user
        if not seller.is_authenticated:
            return Product.objects.none()
        return qs.filter(seller=request.user)
        
    
