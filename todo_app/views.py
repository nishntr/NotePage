from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from todo_app.models import item
from django.urls import reverse, reverse_lazy
from django.utils import timezone
# Create your views here.


class itemListView(ListView):
    model = item
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class itemCreateView(CreateView):
    model = item
    fields = "__all__"
    template_name = "add.html"

    def get_success_url(self):
        return reverse('todo_app:home')


class itemUpdateView(UpdateView):
    model = item
    fields = "__all__"
    template_name = "detail.html"

    def get_success_url(self):
        return reverse('todo_app:home')


class itemDeleteView(DeleteView):
    model = item
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse('todo_app:home')
