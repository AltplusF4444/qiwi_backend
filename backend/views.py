import secrets
import requests
import time
from rest_framework import generics
from rest_framework.response import Response

from .models import *


def get_identification(api_access_token, my_login):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    res = s.get('https://edge.qiwi.com/identification/v1/persons/' + my_login + '/identification')
    return res.json()


def send_p2p(api_access_token, to_qw, sum_p2p):
    s = requests.Session()
    s.headers = {'content-type': 'application/json', 'authorization': 'Bearer ' + api_access_token,
                 'User-Agent': 'Android v3.2.0 MKT', 'Accept': 'application/json'}
    postjson = {"id": "", "sum": {"amount": "", "currency": ""},
                "paymentMethod": {"type": "Account", "accountId": "643"}, "comment": "'+comment+'",
                "fields": {"account": ""}, 'id': str(int(time.time() * 1000))}
    postjson['sum']['amount'] = sum_p2p
    postjson['sum']['currency'] = '643'
    postjson['fields']['account'] = to_qw
    res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments', json=postjson)
    return res.json()


class Seller(generics.GenericAPIView):
    def post(self, request):
        token_pay = request.data['token_pay']
        price = request.data['price']
        phone = "+7" + request.data['phone']
        try:
            client = AuthClients.objects.get(token_app=token_pay)
        except BaseException as ex:
            return Response({
                'exception': 'true'
            })
        else:
            token_qiwi = client.token_qiwi
            sell = send_p2p(token_qiwi, phone, price)
            return Response(sell)


class ReToken(generics.GenericAPIView):
    def post(self, request):
        try:
            phone = request.data['phone']

        except BaseException as be:
            print(be)
        else:
            client = AuthClients.objects.get(number=phone)
            client.token_app = "0"
            flag = True
            while flag:
                t = secrets.token_hex(16)
                flag = False
                c = AuthClients.objects.all()
                for cc in c:
                    if cc.token_app == t:
                        flag = True
                        break
            client.token_app = t
            return Response({
                'token': t
            })


class AuthView(generics.GenericAPIView):

    def post(self, request):

        return Response({
            'token': secrets.token_hex(16),
            'exception': 'false'
        })
