from django.urls import path
from estudio import views

app_name='estudio'
urlpatterns = [
    path('estudios', views.EstudioListView.as_view(), name='estudio-list'),
    path('estudio/add/', views.EstudioCreateView.as_view(), name='estudio-add'),
    path('estudio/<int:pk>/detail', views.EstudioDetailView.as_view(), name='estudio-detail'),
    path('estudio/<int:pk>/update', views.EstudioUpdateView.as_view(), name='estudio-update'),
    path('estudio/<int:pk>/delete', views.EstudioDeleteView.as_view(), name='estudio-delete'),
]