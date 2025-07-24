from django.urls import path
from .views import BookingViewSet

urlpatterns = [
    path('bookings/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('bookings/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
    path('bookings/<int:pk>/accept/', BookingViewSet.as_view({'patch': 'accept'}), name='booking-accept'),
    path('bookings/<int:pk>/reject/', BookingViewSet.as_view({'patch': 'reject'}), name='booking-reject'),
]
