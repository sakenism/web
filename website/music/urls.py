from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #/music/
    url(r'^$', views.index, name = 'index'),


    #/music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
)
