from django.urls import re_path
from .views import page_detail

urlpatterns = [
    re_path(r'^search/(?P<pk>.*)/$', page_detail),
    # re_path(r'^data/(?P<pk>.*)/$', page_detail),
]
