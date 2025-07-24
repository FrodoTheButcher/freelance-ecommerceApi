from rest_framework import serializers
from .models import Booking, BookingItem
from .models import Product
from django.contrib.auth.models import User


class BookingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingItem
        fields = ['id', 'product', 'quantity', 'final_price']


class BookingSerializer(serializers.ModelSerializer):
    items = BookingItemSerializer(many=True)
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Booking
        fields = ['id', 'customer', 'status', 'message', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        booking = Booking.objects.create(customer=self.context['request'].user, **validated_data)
        for item_data in items_data:
            BookingItem.objects.create(booking=booking, **item_data)
        return booking


class BookingStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status', 'message']
