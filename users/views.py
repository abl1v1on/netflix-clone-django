from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import SignUpUserForm, LogInUserForm


class SignUpUserView(CreateView):
    template_name = 'users/signup.html'
    form_class = SignUpUserForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def get_success_url(self):
        return reverse_lazy('user:login')


class LogInUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LogInUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('netflixapp:profiles')


def logout_user(request):
    logout(request)
    return redirect('netflixapp:home')
