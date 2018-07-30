from django.conf.urls import url
from resources import views

urlpatterns = [
    url(r'^' , views.resources, name = 'resources'),
    url(r'^resource1/$' , views.resource1, name = 'resource1'),
    url(r'^resource2/$' , views.resource2, name = 'resource2'),
    url(r'^books/$' , views.books, name = 'books'),
    ]
# Create your views here.
