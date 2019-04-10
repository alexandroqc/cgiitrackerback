import redis
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import SiteUrl
from .serializers import SiteUrlSerializer, SiteURLShortListSerializer
from django.http import JsonResponse
import json
import coreapi
from urllib.parse import quote_plus, urlunparse

pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
client = coreapi.Client()


class SiteUrlViewSet(ModelViewSet):
    serializer_class = SiteUrlSerializer
    queryset = SiteUrl.objects.all()


@api_view(['GET'])
def page_detail(request, pk):
    try:
        uri_encoded = quote_plus(str(pk))
        myurl = r.execute_command('JSON.GET', uri_encoded)
        if myurl is None:
            schema = client.get('http://wappalyzer:3000/api/v1/wapp/'+uri_encoded)
            if schema is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                r.execute_command('JSON.SET', uri_encoded, '.', json.dumps(json.loads(schema)))
                data = json.loads(schema)
        else:
            data = json.loads(myurl)

    except SiteUrl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return JsonResponse(data, status=status.HTTP_200_OK)


class SiteShortURLListViewSet(ModelViewSet):
    queryset = SiteUrl.objects.all()
    serializer_class = SiteURLShortListSerializer

