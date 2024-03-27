from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.urls import reverse

AGE_LIMIT = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('single', 'Single'),
    ('seasonal', 'Seasonal')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True, related_name='user_profiles')


class Profile(models.Model):
    name = models.CharField(max_length=500)
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=500)
    desc = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video', related_name='movie_content')
    cover = models.ImageField(upload_to='covers/')
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=10)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('netflixapp:movie_detail', kwargs={'movie_id': self.uuid})


class Video(models.Model):
    content = models.FileField(upload_to='movies/')

    def __str__(self):
        return str(self.content)