import requests
from airflow.hooks.base import BaseHook
from minio import Minio
import json
from io import BytesIO


def _get_stock_prices(url, symbol, api_key):
    url = f"{url}query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url=url)
    data = response.json()
    return data

def _store_prices(stock):
    minio = BaseHook.get_connection("minio")
    client = Minio(
        endpoint=minio.extra_dejson["endpoint_url"].split('//')[1],
        access_key=minio.login,
        secret_key=minio.password,
        secure=False
    )
    
    bucket_name = 'stock-market'
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    stock = json.loads(stock.replace("'", '"'))
    symbol = stock["Meta Data"]["2. Symbol"]
    data_dic = stock["Time Series (Daily)"]
    data_json = json.dumps(data_dic, ensure_ascii=False).encode("utf8")

    objw = client.put_object(
        bucket_name=bucket_name,
        object_name=f'{symbol}/prices.json',
        data=BytesIO(data_json),
        length=len(data_json)
    )

    return f"{objw.bucket_name}/{symbol}"

