from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']  # ← Заменил name на title


class StockProductSerializer(serializers.ModelSerializer):
    """Сериализатор для промежуточной таблицы (для чтения)."""
    # Вложенный сериализатор для продукта, чтобы отображать его поля внутри склада
    product = ProductSerializer(read_only=True)

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    # Для чтения (GET) выводим вложенный список продуктов
    stock_products = StockProductSerializer(read_only=True, many=True)

    class Meta:
        model = Stock
        # У склада нет поля name/title, есть только address
        fields = ['id', 'address', 'stock_products']

    def create(self, validated_data):
        """Создание нового склада с продуктами."""
        products_data = validated_data.pop('stock_products', [])
        # Создаем склад (тут используется address)
        stock = Stock.objects.create(**validated_data)

        for product_data in products_data:
            StockProduct.objects.create(
                stock=stock,
                product=product_data['product'],
                quantity=product_data['quantity'],
                price=product_data['price']
            )
        return stock

    def update(self, instance, validated_data):
        """Обновление склада и его продуктов."""
        products_data = validated_data.pop('stock_products', None)

        # Обновляем только address
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        if products_data is not None:
            for product_data in products_data:
                StockProduct.objects.update_or_create(
                    stock=instance,
                    product=product_data['product'],
                    defaults={
                        'quantity': product_data['quantity'],
                        'price': product_data['price']
                    }
                )
        return instance