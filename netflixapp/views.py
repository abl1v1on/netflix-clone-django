from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Profile
from .forms import CreateNewProfileForm


def index(request):
    if request.user.is_authenticated:
        return redirect('netflixapp:profiles')
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context)


@login_required
def profile_list(request):
    user_profiles = request.user.profiles.all()

    context = {
        'title': 'Профили',
        'profiles': user_profiles
    }
    return render(request, 'profileList.html', context)


@login_required
def create_new_profile(request):
    if request.user.profiles.count() >= 5:
        return redirect('netflixapp:profiles')
    if request.method == 'POST':
        form = CreateNewProfileForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('netflixapp:profiles')
    else:
        form = CreateNewProfileForm()
    context = {
        'form': form,
        'title': 'Создать новый профиль'
    }
    return render(request, 'profileCreate.html', context)
