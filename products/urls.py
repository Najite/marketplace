from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register('products', views.ProductListApi, basename='products')
router.register('categories', views.CategoryListApi, basename='categories')



urlpatterns = router.urls
