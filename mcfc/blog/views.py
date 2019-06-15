from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['active'] = 'blog'
        return data

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog-detail.html"