from ..models import Product
from ..serializers.serializers_products import ProductSerializer


class RegisterView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = IsAuthenticated