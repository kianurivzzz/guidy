from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Guide


class GuideListView(ListView):
    model = Guide
    queryset = Guide.objects.all().order_by('-date_created')


class GuideDetailView(DetailView):
    model = Guide


class GuideCreateView(CreateView):
    model = Guide
    fields = ['title', 'content']
    success_url = reverse_lazy('guides_list')


class GuideUpdateView(UpdateView):
    model = Guide
    fields = ['title', 'content']

    def get_success_url(self) -> str:
        return reverse_lazy('guide_detail', kwargs={'pk': self.guide.id})


class GuideDeleteView(DeleteView):
    model = Guide
    success_url = reverse_lazy('guides_list')
