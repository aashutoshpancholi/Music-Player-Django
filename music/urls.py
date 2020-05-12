from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #   /music/2/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #   /music/album/add/
    url(r'album/add/$', views.create_album.as_view(), name='create_album'),

    #   /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.update_album.as_view(), name='update_album'),

    #   /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.delete_album.as_view(), name='delete_album'),
]
