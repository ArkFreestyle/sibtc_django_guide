from django.test import TestCase
from django.urls import reverse, resolve
from .views import home


class HomeTests(TestCase):
    """Class for all home page related tests"""

    def test_home_view_status_code(self):
        """Response returned should be 200"""
        
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """Root url (/) should return the home view"""

        view = resolve('/')
        self.assertEquals(view.func, home)