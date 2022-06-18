from django.urls import path
from viaje import views

app_name='viaje'
urlpatterns = [
    path('viajes', views.ViajeListView.as_view(), name='viaje-list'),
    path('viaje/add/', views.ViajeCreateView.as_view(), name='viaje-add'),
    path('viaje/<int:pk>/detail', views.ViajeDetailView.as_view(), name='viaje-detail'),
    path('viaje/<int:pk>/update', views.ViajeUpdateView.as_view(), name='viaje-update'),
    path('viaje/<int:pk>/delete', views.ViajeDeleteView.as_view(), name='viaje-delete'),
]