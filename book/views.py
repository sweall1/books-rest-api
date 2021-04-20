from .models import Books
from .serializers import BookSerializer
from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
import requests


class MultipleAuthorsFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        authors = request.query_params.get('authors')
        if authors:
            authors = authors.split(",")
            return queryset.filter(authors__in=authors)
        return queryset


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    http_method_names = ['get']
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, MultipleAuthorsFilter)
    ordering_fields = ['published_date']
    filterset_fields = {
            'published_date' : ['iexact']
        }

    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

#"Category" is given in url
def post_books(request, category):
    name = category
    Books.objects.all().delete()
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(category)
    response = requests.get(url).json()

    for x in range(len(response['items'])):
        books = Books()
        books.id = response['items'][x].get('id')
        books.title = response['items'][x]['volumeInfo'].get('title')
        books.authors = response['items'][x]['volumeInfo'].get('authors')
        books.published_date = response['items'][x]['volumeInfo'].get('publishedDate')
        books.categories = response['items'][x]['volumeInfo'].get('categories')
        books.average_rating = response['items'][x]['volumeInfo'].get('averageRating')
        books.ratings_count = response['items'][x]['volumeInfo'].get('ratingsCount')
        books.thumbnail = response['items'][x]['volumeInfo']['imageLinks'].get('thumbnail')
        books.save()

    return render(request, 'book/post_books.html', {'name': name})

