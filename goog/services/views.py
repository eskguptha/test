from django.http import HttpResponse
# Rest API
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.core import serializers
import json


@api_view(['GET'])
def stock_rest(request, format=None):
    msg = {}
    if request.method == 'GET' and 'ticker' in request.GET:
        if request.GET.get('ticker').strip() != '':
            q = request.GET.get('ticker')
            payload = {'client': 'iq', 'q': q}
            api_url = "http://finance.google.com/finance/info"
            r = requests.get(api_url, params=payload)
            if r.status_code == 200:
                if "//" in r.text:
                    response_data = r.text[4:]
                else:
                    response_data = r.text
                try:
                    result_data = json.loads(response_data)[0]
                    msg = {
                       "ticker" : result_data['t'],
                       "exchange" : result_data['e'],
                       "lastPrice" : result_data['pcls_fix'],
                       "lastTradeDateTime" : result_data['lt_dts']
                    }
                    return Response(msg, status=r.status_code)
                except (KeyError) as e:
                    msg = {"msg" : "%s"% str(e)}
                    return Response(response_data, status=r.status_code)
            else:
                msg = {"msg" : r.text}
                return Response(msg, status=r.status_code)
        else:
            msg = {"ticker" : "Ticker Required"}
    else:
        msg = {"ticker" : "Ticker Required"}

    return Response(msg, status=status.HTTP_400_BAD_REQUEST)