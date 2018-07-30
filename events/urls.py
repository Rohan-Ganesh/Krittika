from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^events/$' , views.event, name = 'events')]
# Create your views here.
