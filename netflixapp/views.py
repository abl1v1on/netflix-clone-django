from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile, Movie
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


@login_required
def movie_list(request, profile_id):
    profile = get_object_or_404(Profile, uuid=profile_id)
    if profile not in request.user.profiles.all():
        return redirect('netflixapp:home')

    if profile.age_limit == 'All':
        movies = Movie.objects.all()
    else:
        movies = Movie.objects.filter(age_limit=profile.age_limit)

    context = {
        'title': 'Список фильмов',
        'movies': movies
    }
    return render(request, 'movieList.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, uuid=movie_id)

    context = {
        'title': f'{movie.title}',
        'movie': movie
    }
    return render(request, 'movieDetail.html', context)
