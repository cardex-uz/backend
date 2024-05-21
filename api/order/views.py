from rest_framework import viewsets

from api.order.serializers import OrderSerializer, OrderItemSerializer
from order.models import Order, OrderItem


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
