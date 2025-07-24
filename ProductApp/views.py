from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import Product, Category, ProductCategory, Review
from .serializers import (
    ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer, ProductDetailSerializer,
    CategorySerializer, CategoryCreateSerializer, CategoryDetailSerializer,
    ProductCategorySerializer, ProductCategoryCreateSerializer, ProductCategoryDetailSerializer,
    ReviewSerializer, ReviewCreateSerializer, ReviewUpdateSerializer, ReviewDetailSerializer, ReviewListSerializer
)
from .requests import (
    ProductRequestCreateSerializer, ProductRequestUpdateSerializer,
    CategoryRequestCreateSerializer,
    ProductCategoryRequestCreateSerializer,
    ReviewRequestCreateSerializer, ReviewRequestUpdateSerializer
)

# -- PRODUCT VIEWSET --

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ProductUpdateSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    @swagger_auto_schema(request_body=ProductRequestCreateSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ProductRequestUpdateSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ProductRequestUpdateSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


# -- CATEGORY VIEWSET --

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CategoryCreateSerializer
        elif self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategorySerializer

    @swagger_auto_schema(request_body=CategoryRequestCreateSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# -- PRODUCTCATEGORY VIEWSET --

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCategoryCreateSerializer
        elif self.action == 'retrieve':
            return ProductCategoryDetailSerializer
        return ProductCategorySerializer

    @swagger_auto_schema(request_body=ProductCategoryRequestCreateSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# -- REVIEW VIEWSET --

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ReviewUpdateSerializer
        elif self.action == 'retrieve':
            return ReviewDetailSerializer
        return ReviewListSerializer

    @swagger_auto_schema(request_body=ReviewRequestCreateSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ReviewRequestUpdateSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ReviewRequestUpdateSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
