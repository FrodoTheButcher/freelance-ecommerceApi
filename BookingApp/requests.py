from rest_framework import serializers


class BookingItemRequestSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()
    final_price = serializers.DecimalField(max_digits=10, decimal_places=2)


class BookingRequestCreateSerializer(serializers.Serializer):
    items = BookingItemRequestSerializer(many=True)
    message = serializers.CharField(required=False, allow_blank=True)


class BookingStatusUpdateRequestSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=["accepted", "rejected"])
    message = serializers.CharField(required=False, allow_blank=True)


class BookingAcceptRejectRequestSerializer(serializers.Serializer):
    message = serializers.CharField(required=False, allow_blank=True)
