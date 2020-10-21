from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Auto, Make

class AutoListView(LoginRequiredMixin, ListView):
    template_name = 'autos/auto_list.html'
    model = Auto

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['makes_count'] = Make.objects.count()
        return context

class AutoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:auto_list')
    fields = '__all__'
    model = Auto

class AutoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:auto_list')
    fields = '__all__'
    model = Auto

class AutoDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('autos:auto_list')
    model = Auto

class MakeListView(LoginRequiredMixin, ListView):
    template_name = 'autos/make_list.html'
    model = Make

class MakeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:auto_list')
    fields = '__all__'
    model = Make

class MakeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:auto_list')
    fields = '__all__'
    model = Make

class MakeDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('autos:auto_list')
    model = Make
