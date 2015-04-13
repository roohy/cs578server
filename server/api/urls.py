__author__ = 'roohy'

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^status/list/(?P<pk>[0-9]+)/$',views.status_list),
    url(r'^user/$',views.user_list),
    url(r'status/(?P<pk>[0-9]+)/$',views.status_detail),
    url(r'user/(?P<pk>[0-9]+)/$',views.user_detail),
]


