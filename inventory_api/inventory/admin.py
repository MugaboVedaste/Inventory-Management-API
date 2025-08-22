from django.contrib import admin
from .models import InventoryItem, InventoryChangeHistory, Category, User

admin.site.register(InventoryItem)
admin.site.register(InventoryChangeHistory)
admin.site.register(Category)
admin.site.register(User)

# Register your models here.
