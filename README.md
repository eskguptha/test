# test
Connect Database
Random data preperation
Insert records into mysql
Cache buidling


Create a RESTful service that takes stock tickers and returns the stock data. The service can use google finance API to get data

Expected API
curl -iX GET http://localhost:2000/stock?ticker=GOOG

Expected response

{
   "ticker" : "GOOG",
   "exchange" : "NASDAQ",
   "lastPrice" : "921.28",
   "lastTradeDateTime" : "2017-08-24T16:00:04Z"
}

Sample google finance API:

The API can use google finance api to get real time stock data
http://finance.google.com/finance/info?client=ig&q=GOOG


virtualenv goog_env
source goog_env/bin/activate
cd goog
pip install -r pip-requirements.txt
python manage.py runserver
http://127.0.0.1:8000/stock?ticker=GOOG
python manage.py test
