from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ItemSerializer, CategorySerializer, BrandSerializer
from .models import Items, Category, Brand
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                        ListAPIView)

# Create your views here.
class ItemList(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class ItemDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class ItemsByCategory(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Items.objects.filter(category__name=category)

class CategoryList(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class BrandList(ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class BrandDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticated]