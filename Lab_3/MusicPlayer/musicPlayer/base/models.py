from django.db import models
from django.contrib.auth.models import User, UserManager


class Genre(models.Model):
    genre_name = models.CharField(max_length=256)

    def __str__(self):
        return self.genre_name


class Track(models.Model):
    title = models.CharField(max_length=256)
    audioFile = models.FileField()
    artist = models.CharField(max_length=256)
    genre = models.ManyToManyField(Genre)
    description = models.TextField(null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_path(self):
        return self.audioFile


class Listener(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    track_list = models.ManyToManyField(Track, null=True, )

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Listener'
        verbose_name_plural = 'Listeners'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/users', verbose_name='Image')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
