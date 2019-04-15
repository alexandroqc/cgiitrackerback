from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Applications(models.Model):
    name = models.CharField(max_length=255, unique=True)
    confidence = models.PositiveSmallIntegerField(null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True)
    web_site = models.CharField(max_length=300, blank=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'name': self.name,
            'confidence': self.confidence,
            'version': self.version,
            'website': self.web_site,
            'icon': self.icon,
            'categories': self.categories
        }


class SiteUrl(models.Model):
    scheme = models.CharField(max_length=15)
    netloc = models.CharField(max_length=150)
    path = models.CharField(max_length=200, blank=True)
    uri = models.CharField(max_length=400, unique=True)
    applications = models.ManyToManyField(Applications)

    # applications = models.OneToOneField(Applications, on_delete=models.CASCADE)

    def __str__(self):
        return self.netloc

    def to_json(self):
        return {
            'scheme': self.scheme,
            'netloc': self.netloc,
            'path': self.path,
            'uri': self.uri,
            'applications': self.applications
        }
