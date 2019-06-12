import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, render_to_response
from .models import *
from .secret import Public_data, KakaoAPI

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import xmltodict, json

from django.http import HttpResponse


# Create your views here.

class Dabang_List(ListView):
    model = Dabang
    template_name = 'Dabang/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(My_API=KakaoAPI)
        return context



#######################################################################


from django.http import JsonResponse

def dabang_Search(request):
    if request.method == "GET":

        data = request.GET

        add = data['addr[address]']
        zone = data["addr[sigunguCode]"]
        ym = data['ym']
        YM = ''.join(ym.split('-'))
        road_name_Code = data['addr[roadnameCode]']

        sl = data['sl']

        context = {
            'address': add,
            'zonecode': zone,
        }

        context.update(get_info(zone, YM, sl, road_name_Code))

        pprint(context)
        print()

        return JsonResponse(context)



#############################################################


from pprint import pprint

def get_info(LAW, DEAL_YMD, SALE, road_name_Code):
    context = dict()

    sale = {
        '1' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade',
        '2' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade',
        '3' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHTrade',
        '4' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade',
        '5' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade',
        '6' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent',
        '7' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent',
        '8' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent',
        '9' : 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent',
    }

    url = sale[SALE]
    queryParams = 'Dev?' + urlencode({
        quote_plus('ServiceKey'): Public_data,
        quote_plus('pageNo'): '1',
        quote_plus('numOfRows'): '500',
        quote_plus('LAWD_CD'): LAW,
        quote_plus('DEAL_YMD'): DEAL_YMD})

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    dict_type = xmltodict.parse(response_body)
    json_type = json.dumps(dict_type)
    dict_type2 = json.loads(json_type)

    length = int(dict_type2['response']['body']['totalCount'])

    AT_list = []

    for num in range(0, length):
        road = dict_type2['response']['body']['items']['item'][num]['도로명코드']

        if road == road_name_Code:
            AT_list.append(dict_type2['response']['body']['items']['item'][num])

    context = {'list' : AT_list}

    return context

