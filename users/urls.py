from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UserListDetailViewSet

router = DefaultRouter()
router.register(r'register', RegisterView, basename='register')
router.register(r'users', UserListDetailViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),  # Automatically add the generated URLs to your app
]