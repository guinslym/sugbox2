from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name = 'suggies'

urlpatterns = [
    url(r'^activate/(?P<activate_box_key>[0-9A-Za-z-]+)/$', views.activate_box, name='activate_box'),
    #url(r'^sugbox/(?P<slug>[0-9A-Za-z-]+)/$', views.detail_box, name='detail_box'),
    url(r'^$', views.BoxCreateView.as_view(), name='home'),
    url(r'^suggies/$', views.SuggiesCreateView.as_view(), name='add_suggies'),
]
