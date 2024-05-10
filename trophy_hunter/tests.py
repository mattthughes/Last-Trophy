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
        test_user1 = User.objects.create_user(

            username='testuser1', password='1X<ISRUkw+tuK'
            )
        test_game = Game.objects.create(
            title='darksouls',
            slug='dark-souls',
            author=test_user1,
            genre='action',
            trophy_count=50,
            hours=60,
            rating=4.9
        )

        response = self.client.get
        (reverse(
            'game-detail', args=(test_game.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game_detail.html')

    def test_trophy_detail_view(self):
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK'
            )
        test_game = Game.objects.create(
            title='darksouls',
            slug='dark-souls',
            author=test_user1,
            genre='action',
            trophy_count=50,
            hours=60,
            rating=4.9


        )

        test_trophy = Trophies.objects.create(
            title='trophy test',
            slug='trophy-test',
            game=test_game,
            description='checking trophy test works',
            difficulty=1,
            rarity=10.4

        )

        response = self.client.get
        (reverse('trophy-detail', args=(test_trophy.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trophy_detail.html')

    def test_guide_detail_view(self):
        """
        This function is testing the guide
        detail view creating the game, trophies
        and the guide object in the test database
        this is then returning the reverse guide view
        with the argument being the guides primary key
        this is then making sure the correct template
        is being used and the correct response code is
        being returned.
        """
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK'
            )
        test_game = Game.objects.create(
            title='darksouls',
            slug='dark-souls',
            author=test_user1,
            genre='action',
            trophy_count=50,
            hours=60,
            rating=4.9


        )

        test_trophy = Trophies.objects.create(
            title='trophy test',
            slug='trophy-test',
            game=test_game,
            description='checking trophy test works',
            difficulty=1,
            rarity=10.4

        )
        test_guide = Guide.objects.create(
            title='you did it',
            author=test_user1,
            trophy=test_trophy,
            body='testing guide creation works',
            approved=True,
        )

        response = self.client.get(
            reverse('guide-view', args=(test_guide.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guide_detail_view.html')
