from django.urls import path
from .import views
urlpatterns = [
    path('member/<int:pk>', views.UpdateMember.as_view(), name="updatemember"),
    path('member',views.MemberListView.as_view(),name = 'member'),
    path('add-member', views.addmember, name='addmember'),
    path('inactive/<int:pk>', views.inactive, name="inactive"),
]
