from rest_framework import serializers

from api.models import Items, Category, Brand


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'