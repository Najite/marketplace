from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import (
    Category,
    Product,
)
from accounts.serializers import UserSerializers
from . import validators


class CategoryListSerializer(serializers.ModelSerializer):  
    name = serializers.CharField(validators=[validators.validate_name])
    slug = serializers.CharField(validators=[validators.validate_slug])
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ('name',
                  'slug',
                  'products',
                  'url',) 
        depth=1
    
    
    def get_url(self, obj):
        request = self.context['request']
        return {
            'url': reverse('categories-detail',
                           kwargs={'pk':obj.pk},
                           request=request)
        }

class ProductListSerializer(serializers.ModelSerializer):
    seller = UserSerializers(read_only=True)
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('seller', 
                  'name',
                  'image',
                  'price',
                  'category',
                  'url',
                  )
        depth = 1
    
    
    def get_url(self, obj):
        request = self.context['request']
        return {
            'url': reverse('products-detail', 
                           kwargs={'pk':obj.pk},
                           request=request)
        }
    

class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = ('image',)
        


class ProductDetailSerializer(serializers.ModelSerializer):
    seller = UserSerializers(read_only=True)
    class Meta: 
        model = Product
        fields = ('id',
                  'seller',
                  'name',
                  'price',
                  'image',
                  'category',
                  )
        
        


        