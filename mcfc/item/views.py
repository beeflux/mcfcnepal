from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

from .models import Item, ItemCategory, ItemOffer

class ItemListView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'
    paginate_by = 8
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category'] = ItemCategory.objects.all()
        data['active'] = 'item'
        return data
    
    def get_queryset(self):
        items = Item.objects.all()
        if self.request.GET.get('c'):
            items = items.filter(category=self.request.GET.get('c'))
        return items

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item-detail.html'

