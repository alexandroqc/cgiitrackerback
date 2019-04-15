from rest_framework import serializers
from .models import SiteUrl, Applications, Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name')


class ApplicationsSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, required=False)

    def save(self, **kwargs):
        print(kwargs, "*********************")
        return super(ApplicationsSerializer,self).save(**kwargs)

    class Meta:
        model = Applications
        fields = ('id', 'name', 'confidence', 'version', 'icon', 'web_site', 'categories')


class SiteUrlSerializer(serializers.ModelSerializer):
    applications = ApplicationsSerializer(many=True)
    # applications = serializers.HyperlinkedRelatedField(many=True, view_name='site-url-detail')

    def create(self, validated_data):
        applications_data = validated_data.pop('applications')
        site_url = SiteUrl.objects.create(**validated_data)
        for application in applications_data:
            categories_serializer = CategoriesSerializer(data=application['categories'], many=True)
            categories_serializer.is_valid()
            cat = categories_serializer.save()
            application, created = Applications.objects.get_or_create(
                name=application['name'],
                confidence=application['confidence'],
                version=application['version'],
                icon=application['icon'],
                web_site=application['web_site']
            )
            for category in cat:
                application.categories.add(category)
                application.save()
            site_url.applications.add(application)
        return site_url

    class Meta:
        model = SiteUrl
        fields = ('id', 'scheme', 'netloc', 'path', 'uri', 'applications')
        # read_only_fields = ('auth_token',)


class SiteURLShortListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUrl
        fields = ('id', 'scheme', 'netloc', 'path', 'uri')
