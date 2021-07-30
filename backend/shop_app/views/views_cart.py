from ..serializers.serializers_cart import CartSerializer
from ..serializers.serializers_products import ProductSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from ..cart import Cart
from rest_framework.response import Response
from rest_framework import status


class CartViewSet(ViewSet):

    def list(self, request):
        cart = Cart(request)
        serializer = ProductSerializer(cart.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):

        try:

            serializer = CartSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                data = serializer.data

                cart = Cart(request)

                if data['quantity'] is not None:
                    cart.add(data['product_id'], data['quantity'])

                else:
                    cart.add(data['product_id'])

                return Response(status=status.HTTP_200_OK)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except ValueError as err:
            return Response({f'error: {err}'}, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response({f'error: Product not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cart = Cart(request)
        cart.remove(pk)
        return Response(status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False, url_path="get_total_price")
    def get_total_price(self, request):
        cart = Cart(request)
        return JsonResponse({'total_price': cart.get_total_price()})

    @action(methods=["get"], detail=False, url_path="clear")
    def clear(self, request):
        cart = Cart(request)
        cart.clear()
        return Response(status=status.HTTP_200_OK)
