from ..models import Product, Category, Image, Order
from ..serializers.serializers_products import ProductSerializer, CategorySerializer, ImageSerializer, OrderSerializer, \
    OrderCreateSerializer
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsOwner, IsSeller
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.viewsets import ViewSet
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_permissions(self):
    #     if not self.action in ['list', 'retrieve']:
    #         self.permission_classes = [IsAuthenticated, IsAdmin]
    #
    #     return super(self.__class__, self).get_permissions()


class CategoryViewSet(CreateModelMixin,
                      ListModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_permissions(self):
    #     if not self.action in ['list']:
    #         self.permission_classes = [IsAuthenticated, IsAdmin]
    #
    #     return super(self.__class__, self).get_permissions()


# class OrderViewSet(ModelViewSet):
#     serializer_class = OrderCreateSerializer
#     # permission_classes = [IsAuthenticated, IsSeller]
#
#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)
#
#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)
#
#     # def get_permissions(self):
#     #     if self.action in ['retrieve']:
#     #         self.permission_classes = [IsOwner, IsAuthenticated]
#     #
#     #     return super(self.__class__, self).get_permissions()