from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, CreateView
from .models import Gallery

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'

class CreateGalleryView(CreateView):
    model = Gallery
    fields = '__all__'
    template_name = 'gallery/add-gallery.html'
    success_url = reverse_lazy('gallery-view')
