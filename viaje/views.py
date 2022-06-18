from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from viaje.models import Viaje

class ViajeListView(ListView):
    model = Viaje
    template_name = "viaje/viaje_list.html"

class ViajeDetailView(DetailView):
    model = Viaje
    template_name = "viaje/viaje_detail.html"

class ViajeCreateView(CreateView):
    model = Viaje
    success_url = reverse_lazy('viaje:viaje-list')
    fields = ['destino', 'nro_vuelo', 'fecha', 'notas']

class ViajeUpdateView(UpdateView):
    model = Viaje
    success_url = reverse_lazy('viaje:viaje-list')
    fields = ['destino', 'nro_vuelo', 'fecha', 'notas']

class ViajeDeleteView(DeleteView):
    model = Viaje
    success_url = reverse_lazy('viaje:viaje-list')
