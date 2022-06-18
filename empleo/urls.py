from django.urls import path
from empleo import views

app_name='empleo'
urlpatterns = [
    path('empleos', views.EmpleoListView.as_view(), name='empleo-list'),
    path('empleo/add/', views.EmpleoCreateView.as_view(), name='empleo-add'),
    path('empleo/<int:pk>/detail', views.EmpleoDetailView.as_view(), name='empleo-detail'),
    path('empleo/<int:pk>/update', views.EmpleoUpdateView.as_view(), name='empleo-update'),
    path('empleo/<int:pk>/delete', views.EmpleoDeleteView.as_view(), name='empleo-delete'),
]