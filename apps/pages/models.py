from django.db import models


class WebPage(models.Model):
    urls = models.CharField(max_length=255)

    def __unicode__(self):
        return self.urls

    def to_json(self):
        return {
            'urls': self.urls
            # 'id': self.id,
            # 'name': self.name,
            # 'desc': self.description,
            # 'price': self.price,
            # 'date_created': self.date_created,
            # 'date_modified': self.date_modified
        }


class Applications(models.Model):
    name = models.CharField(max_length=255)
    confidence = models.PositiveSmallIntegerField()
    version = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    web_site = models.CharField(max_length=300)
    web_page = models.ForeignKey(WebPage)

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
