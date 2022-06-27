from urllib.request import urlopen
from rest_framework import viewsets, generics
from getxml.serializers import BookSerializer
from .models import books

from rest_framework import filters
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from django.shortcuts import render, redirect, render
import requests
from xml.etree import ElementTree
import xmltodict
import xml.etree.ElementTree as ET

from urllib.parse import urlparse
from urllib.request import urlopen
import xml.etree.ElementTree as ET



# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed / edited or filtered.
    """
    queryset = books.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = {'authors': ['startswith'],'published_date': ['startswith'] }
    search_fields = ['authors','published_date']
    ordering_fields = ['published_date','id']

class BookYearList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the year.
        """
        year = self.kwargs['year']
        return books.objects.filter(published_date = year)

class BookAuthorList(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name.
        """
        authorname = self.kwargs['authorname']
        return books.objects.filter(authors = authorname)

class BookAuthorList2(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        """
        This view should return a list of all the books 
        determined by the author name 1 or author name 2.
        """
        authorname1 = self.kwargs['authorname1']
        authorname2 = self.kwargs['authorname2']
        print(authorname1)
        print(authorname2)
        return books.objects.filter(authors = authorname1).filter(authors = authorname2)

def homepage(request):
    return render(request, 'booksapi/homepage.html')

def getdata1(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
    
    # Read the JSON
    data1 = requests.get(url).json()

    # Create a Django model object for each object in the JSON 
    for book_data in data1['items']:
        volume_info = book_data['volumeInfo']
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']
        categoriesx = volume_info.get("categories", None)
        averageRatingx = volume_info.get("averageRating", None)
        ratingsCountx = volume_info.get("ratingsCount", None)
        thumbnailx = volume_info.get("imageLinks", None)
        #thumbnaily = thumbnailx.get("thumbnail", None)

        book = books.objects.create(
            title=title,authors=authors, 
            published_date=published_date, 
            categories=categoriesx,
            average_rating=ratingsCountx,
            ratings_count = ratingsCountx,
            #thumbnail=thumbnaily,
           )

    return render(request, 'booksapi/data1added.html')

def getdata2(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=war'

    # Read the JSON
    data1 = requests.get(url).json()

    # Create a Django model object for each object in the JSON 
    for book_data in data1['items']:
        volume_info = book_data['volumeInfo']
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']
        categoriesx = volume_info.get("categories", None)
        averageRatingx = volume_info.get("averageRating", None)
        ratingsCountx = volume_info.get("ratingsCount", None)
        thumbnailx = volume_info.get("imageLinks", None)
        thumbnaily = thumbnailx.get("thumbnail", None)
     
        book = books.objects.create(
            title=title,authors=authors, 
            published_date=published_date, 
            categories=categoriesx,
            average_rating=ratingsCountx,
            ratings_count = ratingsCountx,
            thumbnail=thumbnaily,
           )
           
    return render(request, 'booksapi/data2added.html')

def getdata3(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q=war'
    data1 = requests.get(url).json()

    with urlopen('https://pypi.org/rss/packages.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        #print(len(root[0].tag)
        #print(root[0][5][0].text)
        print('----------------------------')
        xc = 5
        while xc < 10:
            for child in root[0][xc]:
                #print('CT:',child.tag,'CT:',child.text,)
                if child.tag == 'author':
                    xc_author = child.text
                if child.tag == 'title':
                    xc_title = child.text
                if child.tag == 'pubDate':
                    xc_pubDate = child.text

            book = books.objects.create(
                title=xc_title,
                authors=xc_author,
                published_date=xc_pubDate
                #categories=categoriesx,
                #average_rating=ratingsCountx,
                #ratings_count = ratingsCountx,
            )
            xc = xc + 1 
    # Read the JSON


    '''
    # Create a Django model object for each object in the JSON 
    for book_data in data1['items']:
        volume_info = book_data['volumeInfo']
        title = volume_info['title']
        authors = volume_info['authors']
        published_date = volume_info['publishedDate']
        categoriesx = volume_info.get("categories", None)
        averageRatingx = volume_info.get("averageRating", None)
        ratingsCountx = volume_info.get("ratingsCount", None)
        thumbnailx = volume_info.get("imageLinks", None)
        thumbnaily = thumbnailx.get("thumbnail", None)
     
        book = books.objects.create(
            title=title,authors=authors, 
            published_date=published_date, 
            categories=categoriesx,
            average_rating=ratingsCountx,
            ratings_count = ratingsCountx,
            thumbnail=thumbnaily,
           )
    '''
           
    return render(request, 'booksapi/data2added.html')

def deletedata2(request):
    for booksx in books.objects.all():
        if booksx.id > 11:
            booksx.delete()
    return render(request, 'booksapi/data2deleted.html')
