from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Booking
from .serializers import BookingSerializer, BookingStatusUpdateSerializer
from .requests import (
    BookingRequestCreateSerializer,
    BookingStatusUpdateRequestSerializer,
    BookingAcceptRejectRequestSerializer
)


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.customer == request.user


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Booking.objects.filter(customer=user)
        return Booking.objects.none()


    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return BookingStatusUpdateSerializer if self.request.user.is_staff else BookingSerializer
        return BookingSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @swagger_auto_schema(request_body=BookingRequestCreateSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=BookingStatusUpdateRequestSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=BookingStatusUpdateRequestSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(method='patch', request_body=BookingAcceptRejectRequestSerializer)
    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAdminUser])
    def accept(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'accepted'
        booking.message = request.data.get('message', '')
        booking.save()
        return Response({'status': 'accepted', 'message': booking.message})

    @swagger_auto_schema(method='patch', request_body=BookingAcceptRejectRequestSerializer)
    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk=None):
        booking = self.get_object()
        booking.status = 'rejected'
        booking.message = request.data.get('message', '')
        booking.save()
        return Response({'status': 'rejected', 'message': booking.message})
