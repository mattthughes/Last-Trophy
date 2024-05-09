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
        """
        This function is getting the game url
        and returning the reverse making sure
        the correct template and response code
        has been returned.
        """
        response = self.client.get(self.game_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_view_url_accessible_by_name(self):
        """
        This function is returning the url by name
        and the response code.
        """
        response = self.client.get(reverse('game'))
        self.assertEqual(response.status_code, 200)


    def test_game_detail_view(self):
        """
        This function is creating an author
        for the game object and then creating
        a game in the test database after this
        it is returning the reverse titled game
        detail and this slug along with the
        template and response code.
        """
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
