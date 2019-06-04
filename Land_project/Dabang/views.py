import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

from django.views.generic import ListView
from .models import *


# Create your views here.

class Dabang_List(ListView):
    model = Dabang
    template_name = 'Dabang/index.html'



from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from pprint import pprint
import xml.etree.ElementTree as ET


def get_info():

    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
    queryParams = '?' + urlencode({
        quote_plus('ServiceKey'): serviceKey,
        quote_plus('pageNo'): '1',
        quote_plus('numOfRows'): '10',
        quote_plus('LAWD_CD'): '11110',
        quote_plus('DEAL_YMD'): '201512'})

    request = Request(url + queryParams)

    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()



get_info()