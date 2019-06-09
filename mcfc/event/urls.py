from django.urls import path
from . import views
urlpatterns = [
    path('events', views.EventListView.as_view(), name="events"),
    path('add-events', views.EventAddView.as_view(), name="add-events"),
    path('events/<int:pk>', views.EventDetailView.as_view(), name="detail-event"),
    path('pastevents', views.PastEventListView.as_view(), name="past-events"),
     path('pastevents/<int:pk>', views.EventDetailView.as_view(), name="past-events"),
]