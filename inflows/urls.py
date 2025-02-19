from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflows_list'),
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflows_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflows_detail'),
    
    path('api/v1/inflows/', views.InflowCreateListAPIView.as_view(), name='inflows-create-list-api-view'),
    path('api/v1/inflows/<int:pk>/', views.InflowsRetrive.as_view(), name='inflows-detail-api-view'),
]