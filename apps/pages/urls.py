from django.urls import re_path
from .views import page_detail

from rest_framework.routers import DefaultRouter
from .views import SiteUrlViewSet, SiteShortURLListViewSet

router = DefaultRouter()
router.register(r'urlinfo', SiteUrlViewSet)
router.register(r'urlshortlist', SiteShortURLListViewSet)

urlpatterns = [
    re_path(r'^search/(?P<pk>.*)/$', page_detail),
    re_path(r'^urlsite/(?P<pk>.*)/$', page_detail),
    # re_path(r'^urlsitecache/(?P<schema>.*)/(?P<netloc>.*)/(?P<pathname>.*)$', page_detail_cache),
]

urlpatterns += router.urls
