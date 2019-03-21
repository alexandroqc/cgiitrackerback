from rest_framework import serializers
from .models import SiteUrl


class SiteUrlSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     site_url = serializers.HyperlinkedModelSerializer

    class Meta:
        model = SiteUrl
        fields = ('id', 'scheme', 'netloc', 'path')
        # read_only_fields = ('auth_token',)
