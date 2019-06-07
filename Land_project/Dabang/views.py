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




class Dabang_search(View):
    pass

from django.http import JsonResponse

def dabang_Search(request):
    if request.method == "GET":
        data = request.GET
        print(data)

        # print(data['addr[address]'])
        # print(data["addr[zonecode]"])
        add = data['addr[address]']
        zone = data["addr[sigunguCode]"]

        print(add, zone)


        context = {
            'address': add,
            'zonecode': zone,
        }

        print()
        print()
        print()

        context.update(get_info(zone))

        # return render(request, 'Dabang/search_list.html', context)
        # return render(request, 'Dabang/search_list.html')
        return JsonResponse(context)

from pprint import pprint

def get_info(LAW):
    context = dict()

    # serviceKey = 'iW7CmOM8mzRIMTwitueEeqdoxZm7NVxjMnHA7+8j8T3aTt+J3DGYbMVRjcJhX7j5D7O7sg7AWG7m1RE14GmbvA=='

    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    queryParams = '?' + urlencode({
        quote_plus('ServiceKey'): Public_data,
        quote_plus('pageNo'): '1',
        quote_plus('numOfRows'): '20',
        quote_plus('LAWD_CD'): LAW,
        quote_plus('DEAL_YMD'): '201512'})


    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    dict_type = xmltodict.parse(response_body)
    json_type = json.dumps(dict_type)
    dict_type2 = json.loads(json_type)



    price = dict_type2['response']['body']['items']['item'][0]['거래금액']
    name = dict_type2['response']['body']['items']['item'][0]['아파트']
    year = dict_type2['response']['body']['items']['item'][0]['년']
    month = dict_type2['response']['body']['items']['item'][0]['월']
    day = dict_type2['response']['body']['items']['item'][0]['일']
    floor = dict_type2['response']['body']['items']['item'][0]['층']

    context.update(
        price=dict_type2['response']['body']['items']['item'][0]['거래금액'],
        name=dict_type2['response']['body']['items']['item'][0]['아파트'],
        year=year,
        month=month,
        day=day,
        floor=floor,
    )

    pprint(dict_type2['response']['body']['items']['item'][0]['거래금액'])
    print()
    print()
    print()
    print()
    return context

