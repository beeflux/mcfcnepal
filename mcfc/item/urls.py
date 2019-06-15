from django.urls import path
from . import views
urlpatterns = [
    path('item',views.ItemListView.as_view(),name="item"),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name="item-details"),
]