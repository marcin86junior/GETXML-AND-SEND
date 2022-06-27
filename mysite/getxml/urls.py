from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from getxml import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('bookspublished_date=<year>', views.BookYearList.as_view()),
    path('booksauthor=<authorname>', views.BookAuthorList.as_view()),
    path('booksauthor=<authorname1>/author=<authorname2>', views.BookAuthorList2.as_view()),
    path('bookshomepage/', views.homepage),
    path('bookshomepage/addbooks1/', views.getdata1),
    path('bookshomepage/addbooks2/', views.getdata2),
    path('bookshomepage/addbooks3/', views.getdata3),
    path('bookshomepage/deletebooks2/', views.deletedata2),
]