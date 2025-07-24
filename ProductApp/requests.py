from rest_framework import serializers


# -- PRODUCT REQUEST CLASSES --

class ProductRequestCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    categories = serializers.ListField(child=serializers.IntegerField())


class ProductRequestUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    stock = serializers.IntegerField(required=False)
    categories = serializers.ListField(child=serializers.IntegerField(), required=False)


# -- CATEGORY REQUEST CLASSES --

class CategoryRequestCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)


# -- PRODUCTCATEGORY REQUEST CLASSES --

class ProductCategoryRequestCreateSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    category = serializers.IntegerField()


# -- REVIEW REQUEST CLASSES --

class ReviewRequestCreateSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    user = serializers.CharField()
    rating = serializers.IntegerField()
    comment = serializers.CharField(required=False)


class ReviewRequestUpdateSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    comment = serializers.CharField(required=False)
