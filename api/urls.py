from django.urls import path
from .views import (ItemList, ItemDetail, ItemsByCategory, CategoryList, CategoryDetail,
                    BrandList, BrandDetail)

urlpatterns = [
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
    path('items/<str:category>/', ItemsByCategory.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('brands/', BrandList.as_view()),
    path('brands/<int:pk>/', BrandDetail.as_view()),
]