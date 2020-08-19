from django.conf.urls import url
from spotify import views
urlpatterns = [
    url(r'^api/spotify/login$', views.login),
    url(r'^api/spotify/playlist$', views.getPlaylist),
]