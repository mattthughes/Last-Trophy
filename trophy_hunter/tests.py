from django.test import TestCase, Client
from django.urls import reverse
from .models import Game, Trophies, Guide
import json
from django.contrib.auth import get_user_model
User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.game_url = reverse('game')
        
    
    def test_game_view_GET(self):
        response = self.client.get(self.game_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('game'))
        self.assertEqual(response.status_code, 200)


    def test_game_detail_view(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test = Game.objects.create(
            title='darksouls',
            slug = 'dark-souls',
            author= test_user1,
            genre= 'action',
            trophy_count= 50,
            hours = 60,
            rating= 4.9


        )

        response = self.client.get(reverse('game-detail', args=(test.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_detail.html')
