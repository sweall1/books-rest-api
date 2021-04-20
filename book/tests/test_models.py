from django.test import TestCase
from book.models import Books


class TestModel(TestCase):

    def setUp(self):
        self.book1 = Books.objects.create(
            id='it',
            title='should',
            authors='work',
            published_date='2020',
            categories='was',
            ratings_count='2',
            average_rating='5',
            thumbnail='good'
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEquals(self.book1.slug, 'book-1')