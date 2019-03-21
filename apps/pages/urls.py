from django.urls import re_path
from .views import page_detail

from rest_framework.routers import DefaultRouter
from .views import SiteUrlViewSet

router = DefaultRouter()
router.register(r'urlinfo', SiteUrlViewSet)

urlpatterns = [
    re_path(r'^search/(?P<pk>.*)/$', page_detail),
    re_path(r'^urlsite/(?P<pk>.*)/$', page_detail),
]

urlpatterns += router.urls
