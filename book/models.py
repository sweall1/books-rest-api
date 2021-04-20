from django.db import models


class Books(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, null=True)
    authors = models.CharField(max_length=100, null=True)
    published_date = models.CharField(max_length=100, null=True)
    categories = models.CharField(max_length=100, null=True)
    ratings_count = models.CharField(max_length=100, null=True)
    average_rating = models.CharField(max_length=100, null=True)
    thumbnail = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title