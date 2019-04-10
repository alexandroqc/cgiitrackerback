from rest_framework import serializers
from .models import SiteUrl, Applications, Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name')


class ApplicationsSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)

    class Meta:
        model = Applications
        fields = ('id', 'name', 'confidence', 'version', 'icon', 'web_site', 'categories')


class SiteUrlSerializer(serializers.ModelSerializer):
    applications = ApplicationsSerializer(many=True)
    # applications = serializers.HyperlinkedRelatedField(many=True, view_name='site-url-detail')

    class Meta:
        model = SiteUrl
        fields = ('id', 'scheme', 'netloc', 'path', 'uri', 'applications')
        # read_only_fields = ('auth_token',)


class SiteURLShortListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUrl
        fields = ('id', 'scheme', 'netloc', 'path', 'uri')
