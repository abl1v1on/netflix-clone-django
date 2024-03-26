from django.urls import path

from . import views

app_name = 'netflixapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('profiles/', views.profile_list, name='profiles'),
    path('profiles/create-new-profile/', views.create_new_profile, name='create_new_profile'),
]

