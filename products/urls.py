from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("reviews/", views.review_view, name="review_view"),

    path('product-apiview/', views.ProductView.as_view(), name='product'),
    path('product-apiview/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),

    path('products-genericapiview/', views.ProductAPIView.as_view(), name="products_genericapiview"),
    path('products-genericapiview/<int:pk>', views.ProductAPIView.as_view(), name='product_genericapiview'),
]