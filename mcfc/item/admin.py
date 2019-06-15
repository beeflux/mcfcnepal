from django.contrib import admin

# Register your models here.
from .models import Item, ItemCategory, ItemOffer
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemOffer)