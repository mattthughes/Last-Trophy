from django.test import TestCase, Client
from django.urls import reverse
from .models import Game, Trophies, Guide
import json


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
    
