from django.conf.urls import url, include
from home import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^', views.index, name = 'index'),
    #url(r'^home/form', views.new_post),
    url(r'^home', views.homepage, name = 'home'),
    url(r'^events', views.events, name = 'events'),
    url(r'^photos', views.photos, name = 'photos'),
    url(r'^announcements', views.announce, name = 'announcements'),
    url(r'^resources/', views.resources, name = 'resources'),
    url(r'^resource1', views.resource1, name = 'resource1'),
    url(r'^resource2', views.resource2, name = 'resource2'),
    url(r'^books', views.books, name = 'books'),
    url(r'^telescope', views.telescope, name = 'telescope'),
    url(r'^team', views.team, name = 'team'),
    
    ]
# Create your views here.
