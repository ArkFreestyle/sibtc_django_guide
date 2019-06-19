from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, board_topics
from .models import Board


class HomeTests(TestCase):
    """Class for all home page related tests"""

    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        """Response returned should be 200"""
        
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """Root url (/) should return the home view"""

        view = resolve('/')
        self.assertEquals(view.func, home)
    
    def test_home_view_contains_links_to_topics_page(self):
        """Clicking home should link to home"""

        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    """Class for all Board related tests"""

    def setUp(self):
        """Create a test board"""

        Board.objects.create(name='Django', description='Django Board.')

    def test_board_topics_view_success_status_code(self):
        """Response returned should be 200"""

        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        """Response should be 404"""

        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        """Testing whether the correct view function is being used"""

        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{}"'.format(homepage_url))
        