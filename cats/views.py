from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Cat, Breed

class CatListView(LoginRequiredMixin, ListView):
    template_name = 'cats/cat_list.html'
    model = Cat

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['breeds_count'] = Breed.objects.count()
        return context

class CatCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'
    model = Cat

class CatUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'
    model = Cat

class CatDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('cats:cat_list')
    model = Cat

class BreedListView(LoginRequiredMixin, ListView):
    template_name = 'cats/breed_list.html'
    model = Breed

class BreedCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'
    model = Breed

class BreedUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cat_list')
    fields = '__all__'
    model = Breed

class BreedDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('cats:cat_list')
    model = Breed
