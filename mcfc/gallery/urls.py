from django.urls import path
from . import views
urlpatterns = [
    path('gallery', views.GalleryListView.as_view(), name="gallery-view"),
    path('add-gallery', views.CreateGalleryView.as_view(), name="add-gallery")
]