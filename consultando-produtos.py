import pandas as pd
from woocommerce import API

wcapi = API(
    url='http://localhost/python',
    consumer_key='ck_1ff31faf3a078c3f483f620473d780d0402313c5',
    consumer_secret='cs_fee5f5349926f9d5b486b6c12a5df42593a99eb5',
    version="wc/v3",
    timeout=30
)
# Consultar todos os produtos em estoque em todas as páginas
page = 1
per_page = 10
while page < :
    all_products = []
    response = wcapi.get("products", params={"page": page, "per_page": per_page, "stock_status": "instock"})
    products_on_page = response.json()


    print(products_on_page)
print(len(products_on_page))