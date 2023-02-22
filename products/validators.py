from rest_framework import serializers
from .models import Category

def validate_name(value):
    qs = Category.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'Category with the name {value} exists')
    return value

def validate_slug(value):
    qs = Category.objects.filter(slug__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'Slug with the name {value} exists')
    return value