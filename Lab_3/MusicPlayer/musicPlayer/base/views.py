from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Track


# Create your views here.
def home(request):
    return render(request, "base/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'base/signup.html'


class TrackList(LoginRequiredMixin, ListView):
    model = Track
    context_object_name = 'tracklist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['home'] = context['home'].filter(title__icontains=search_input) | context['home'].filter(
                artist__icontains=search_input)
            context['search_input'] = search_input
        return context


class TrackDetail(DetailView):
    model = Track
    context_object_name = 'tracklist'
    template_name = 'base/track_detail.html'


class TrackCreate(CreateView):
    model = Track
    template_name = 'base/track_create.html'
    fields = ['title', 'artist', 'genre', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TrackCreate, self).form_valid(form)


class TrackUpdate(UpdateView):
    model = Track
    fields = ['title', 'artist', 'genre', 'description']
    success_url = reverse_lazy('home')


class TrackDelete(LoginRequiredMixin, DeleteView):
    model = Track
    context_object_name = 'tracklist'
    success_url = reverse_lazy('home')


class AboutSite(ListView):
    model = Track
    template_name = 'base/about.html'