from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("reviews/", views.review_view, name="review_view"),
]