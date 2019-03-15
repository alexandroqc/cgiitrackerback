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
            'webpage': self.web_page
        }


class WebPage(models.Model):
    urls = models.CharField(max_length=255, primary_key=True)
    applications = models.OneToOneField(Applications, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.urls

    def to_json(self):
        return {
            'urls': self.urls,
            'applications': self.applications
        }
