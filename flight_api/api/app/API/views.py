from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from app.models import Detail
from app.API.serializers import DetailSerializer
from Scraping.main import GetDatas
from django.http import JsonResponse, HttpResponse

def data_list(request, cities, date):
    data = GetDatas.data_inputs(cities, date)
    return JsonResponse(data, safe=False)

def data_cities(request):
    data = GetDatas.allCitiesCreateData()
    return JsonResponse(data, safe=False)