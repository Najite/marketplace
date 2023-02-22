from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=True, unique=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(User, related_name='seller',
    
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.FileField(null=True)
    price = models.DecimalField(default=0, decimal_places=2,
                                max_digits=10,)
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.PROTECT
                                 )
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-price']
        indexes = [
            models.Index(fields=['name', 'price'])
        ]
    
    def __str__(self):
        return self.name
    
    
