# author = 'jek'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    # url(r'^start/$', views.start, name='start'),
]