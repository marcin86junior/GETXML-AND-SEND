from django.db import models

# Create your models here.

class books(models.Model):
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=50)
    published_date = models.CharField(max_length=50)
    categories = models.CharField(max_length=50, null=True)
    average_rating = models.CharField(max_length=50, null=True)
    ratings_count = models.CharField(max_length=50, null=True)
    thumbnail = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
