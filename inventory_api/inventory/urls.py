# inventory/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import InventoryItemViewSet, ItemHistoryView, RegisterView, UserDetailView, UserUpdateView, UserDeleteView


router = DefaultRouter()
router.register(r'items', InventoryItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
    path('items/<int:pk>/history/', ItemHistoryView.as_view(), name='item-history'),

    # User management
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', obtain_auth_token, name='user-login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
