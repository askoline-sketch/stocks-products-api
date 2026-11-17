from rest_framework import viewsets, filters
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']  # ← Заменил name на title


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.SearchFilter]
    # Ищем по названию и описанию ПРОДУКТА (у продукта поле title)
    search_fields = ['stock_products__product__title', 'stock_products__product__description']