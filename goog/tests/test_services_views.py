import json
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase
from services.views import stock_rest
import json



class ServiceTest(TestCase):

    def setUp(self):
        self.client = Client()


    def test_200(self):
        response = self.client.get("%s%s"%(reverse('stock_rest'),"?ticker=GOOG"))
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content)
        self.assertIn('ticker', response_data)
        self.assertIn('exchange', response_data)
        self.assertIn('lastPrice', response_data)
        self.assertIn('lastTradeDateTime', response_data)

    def test_400(self):
        response = self.client.get("%s%s"%(reverse('stock_rest'),"?ticker="))
        self.assertEqual(400, response.status_code)
        self.assertEqual('{"ticker":"Ticker Required"}', response.content)