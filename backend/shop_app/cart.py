from decimal import Decimal
from django.conf import settings
from .models import Product
from django.forms.models import model_to_dict


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product = Product.objects.get(pk=product_id)

        if str(product_id) not in self.cart:
            self.cart[product_id] = model_to_dict(product)
            self.cart[product_id]['quantity'] = quantity
        else:
            quantity_sum = self.cart[str(product_id)]['quantity'] + quantity

            if product.quantity < quantity_sum:
                raise ValueError("There is not enough product available")

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_queryset(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
             product.quantity = self.cart[str(product.pk)]["quantity"]

        return products

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()