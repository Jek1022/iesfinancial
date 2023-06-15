# __author__ = 'Grace Villanueva'

from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/pdf/$', views.Pdf.as_view(), name='pdf'),
    url(r'^savedetailtemp/$', views.savedetailtemp, name='savedetailtemp'),
    url(r'^deletedetailtemp/$', views.deletedetailtemp, name='deletedetailtemp'),

    # @change add report urls
    url(r'^report/$', views.ReportView.as_view(), name='report'),
    url(r'^reportresult/$', views.ReportResultView.as_view(), name='reportresult'),
    url(r'^reportresultxlsx/$', views.reportresultxlsx, name='reportresultxlsx'),
]

