from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from estudio.models import Estudio

class EstudioListView(ListView):
    model = Estudio
    template_name = "estudio/estudio_list.html"

class EstudioDetailView(DetailView):
    model = Estudio
    template_name = "estudio/estudio_detail.html"

class EstudioCreateView(CreateView):
    model = Estudio
    success_url = reverse_lazy('estudio:estudio-list')
    fields = ['universidad', 'anio_inicio', 'titulo', 'finalizado']

class EstudioUpdateView(UpdateView):
    model = Estudio
    success_url = reverse_lazy('estudio:estudio-list')
    fields = ['universidad', 'anio_inicio', 'titulo', 'finalizado']

class EstudioDeleteView(DeleteView):
    model = Estudio
    success_url = reverse_lazy('estudio:estudio-list')
