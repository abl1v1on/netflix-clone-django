from django.urls import path

from . import views

app_name = 'netflixapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('profiles/', views.profile_list, name='profiles'),
    path('profiles/create-new-profile/', views.create_new_profile, name='create_new_profile'),
    path('movie-list/<str:profile_id>/', views.movie_list, name='movie_list'),
    path('movie/<str:movie_id>/', views.movie_detail, name='movie_detail'),
    path('watch-movie/<str:movie_id>/', views.movie_watch, name='movie_watch'),

    path('api/movie-list/', views.movie_list_api, name='api_movie_list'),
]
