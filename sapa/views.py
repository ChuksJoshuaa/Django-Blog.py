from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import sapamode
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .forms import sapaform, Rawsapaform


# Create your views here.

class listview(ListView):
    template_name = "sapa_list.html"
    queryset = sapamode.objects.all()

class detailview(DetailView):
    template_name = "sapa_detail.html"
    queryset = sapamode.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(sapamode, id=id)


class createview(CreateView):
    template_name = "sapa_create.html"
    form_class = sapaform
    queryset = sapamode.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


