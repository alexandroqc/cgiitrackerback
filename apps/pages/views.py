import redis
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SiteUrl
from django.http import JsonResponse
import json

pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@api_view(['GET'])
def page_detail(request, pk):
    try:
        myurl = r.execute_command('JSON.GET', str(pk))
        if myurl is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = json.loads(myurl)

    except SiteUrl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # return HttpResponse(json.dumps(data), content_type='application/json')
        return JsonResponse(data, status=status.HTTP_200_OK)
