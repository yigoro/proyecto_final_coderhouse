from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from empleo.models import Empleo

class EmpleoListView(ListView):
    model = Empleo
    template_name = "empleo/empleo_list.html"

class EmpleoDetailView(DetailView):
    model = Empleo
    template_name = "empleo/empleo_detail.html"
    fields = ['empresa', 'periodo', 'puesto']

class EmpleoCreateView(LoginRequiredMixin, CreateView):
    model = Empleo
    success_url = reverse_lazy('empleo:empleo-list')
    fields = ['empresa', 'periodo', 'puesto']

class EmpleoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleo
    success_url = reverse_lazy('empleo:empleo-list')
    fields = ['empresa', 'periodo', 'puesto']

class EmpleoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleo
    success_url = reverse_lazy('empleo:empleo-list')
