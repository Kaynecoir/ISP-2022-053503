from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from .models import Track, Genre


class TrackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password'
        )

        self.track = Track.objects.create(
            title='Название',
            artist = 'Группа',
            genre = 'Рок',
            description = 'Описание',
        )

    def test_string_representation(self):
        self.track = Track(title='Название')
        self.assertEqual(str(self.track), self.track.title)

    def test_get_absolute_url(self):  # new
        self.assertEqual(self.track.get_absolute_url(), '/track/1/')

    def test_track_content(self):
        self.assertEqual(f'{self.track.title}', 'Название')
        self.assertEqual(f'{self.track.artist}', 'Группа')
        self.assertEqual(f'{self.track.genre}', 'Рок')
        self.assertEqual(f'{self.track.description}', 'Описание')

    def test_track_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Some news from test and Hello world!')
        self.assertTemplateUsed(response, 'base/home.html')

    def test_news_detail_view(self):
        response = self.client.get(reverse('home'))
        no_response = self.client.get('/track/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Название')
        self.assertTemplateUsed(response, 'base/home.html')

    def test_post_update_view(self):
        response = self.client.post(reverse('track-update', args='4'), {
            'title': 'Updated title',
            'artist': 'Updated artist',
            'genre': 'genre',
            'description': 'description'
        })
        for post in Track.objects.all():
            print(f"---{post.pk}---")
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('track-delete', args='4'))
        self.assertEqual(response.status_code, 302)
