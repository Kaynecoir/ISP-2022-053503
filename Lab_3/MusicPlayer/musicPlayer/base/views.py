from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, FormView, View

# Create your views here.
def home(request):
    return render(request, "base/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'base/signup.html'

'''class Login(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'base/login.html'
    '''

