from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm


def index(request):
    data = {
        'title': 'Home page',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('sign_in')

    def form_valid(self, form):
        user= form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class= LoginUserForm
    template_name='main/login.html'

def logout_user(request):
    logout(request)
    return redirect('home')