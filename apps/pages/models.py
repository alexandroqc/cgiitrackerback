from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=255)
    confidence = models.PositiveSmallIntegerField()
    version = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    web_site = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    def to_json(self):
        return {
            'name': self.name,
            'confidence': self.confidence,
            'version': self.version,
            'website': self.web_site,
        }


class SiteUrl(models.Model):
    scheme = models.CharField(max_length=15)
    netloc = models.CharField(max_length=150)
    path = models.CharField(max_length=200, blank=True)
    # applications = models.OneToOneField(Applications, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.netloc

    def to_json(self):
        return {
            'scheme': self.scheme,
            # 'applications': self.applications
        }
