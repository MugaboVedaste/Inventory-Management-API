# inventory/views.py
from rest_framework import viewsets, permissions,filters, generics
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem, InventoryChangeHistory, Category, User
from .serializers import InventoryItemSerializer, InventoryChangeHistorySerializer, CategorySerializer, UserSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['supplier', 'category']       # ?supplier=Acme
    search_fields = ['name', 'supplier']              # ?search=Acme
    ordering_fields = ['name', 'price', 'quantity']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ItemHistoryView(generics.ListAPIView):
    serializer_class = InventoryChangeHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryChangeHistory.objects.filter(item_id=self.kwargs['pk'])
    

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"