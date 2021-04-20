from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books

        fields = [
            'id',
            'title',
            'authors',
            'published_date',
            'categories',
            'ratings_count',
            'average_rating',
            'thumbnail',
        ]
