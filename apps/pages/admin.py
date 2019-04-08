from django.contrib import admin
from apps.pages.models import SiteUrl, Applications, Categories

admin.site.register(SiteUrl)
admin.site.register(Applications)
admin.site.register(Categories)
