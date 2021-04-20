from django.test import SimpleTestCase
from django.urls import reverse, resolve
from book.views import post_books


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('post_books')
        self.assertEquals(resolve(url).func, post_books)
