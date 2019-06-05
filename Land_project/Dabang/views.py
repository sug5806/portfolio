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

def dabang_Search(request):
    if request.method == "GET":
        return render_to_response('Dabang/search_list.html')


    if request.is_ajax():
        data = request.POST

        # return render(request,'Dabang/search_list.html',)
        return HttpResponse("OK")



def get_info():
    # serviceKey = 'iW7CmOM8mzRIMTwitueEeqdoxZm7NVxjMnHA7+8j8T3aTt+J3DGYbMVRjcJhX7j5D7O7sg7AWG7m1RE14GmbvA=='

    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    queryParams = '?' + urlencode({
        quote_plus('ServiceKey'): Public_data,
        quote_plus('pageNo'): '1',
        quote_plus('numOfRows'): '20',
        quote_plus('LAWD_CD'): '11110',
        quote_plus('DEAL_YMD'): '201512'})

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    dict_type = xmltodict.parse(response_body)
    json_type = json.dumps(dict_type)
    dict_type2 = json.loads(json_type)
    print(dict_type2)
