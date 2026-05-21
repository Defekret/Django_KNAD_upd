from django.urls import re_path as url
from . import views


urlpatterns = [
    url(r'^$', views.PhoneListView.as_view(), name='phones'),
    url(r'^(?P<pk>\d+)$', views.PhoneDetailView.as_view(), name='phone-detail'),
    url(r'^compare$', views.PhoneCompareView.as_view(), name='compare'),
]
