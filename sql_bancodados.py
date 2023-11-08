import pandas as pd
from sqlalchemy import create_engine

# Criando uma conexão com o banco de dados
engine = create_engine('sqlite:///banco_dados_olist.sqlite')


# Lendo o arquivo "customers" e adicionando no banco de dados
df_customer = pd.read_csv('Archives/olist_customers_dataset.csv')
df_customer.to_sql('customers', engine, if_exists='replace', index=False)


# Lendo o arquivo "geolocation" e adicionando no banco de dados
df_geolocation = pd.read_csv('Archives/olist_geolocation_dataset.csv')
df_geolocation.to_sql('geolocation', engine, if_exists='replace', index=False)


# Lendo o arquivo "order_items" e adicionando no banco de dados
df_order_items = pd.read_csv('Archives/olist_order_items_dataset.csv')

df_order_items.to_sql('order_items', engine, if_exists='replace', index=False)


# Lendo o arquivo "order_payments" e adicionando no banco de dados
df_order_payments = pd.read_csv('Archives/olist_order_payments_dataset.csv')

df_order_payments.to_sql('order_payments', engine, if_exists='replace', index=False)


# Lendo o arquivo "order_reviews" e adicionando no banco de dados
df_order_reviews = pd.read_csv('Archives/olist_order_reviews_dataset.csv')

df_order_reviews.to_sql('order_reviews', engine, if_exists='replace', index=False)


# Lendo o arquivo "orders" e adicionando no banco de dados
df_orders = pd.read_csv('Archives/olist_orders_dataset.csv')

df_orders.to_sql('orders', engine, if_exists='replace', index=False)


# Lendo o arquivo "products" e adicionando no banco de dados
df_products = pd.read_csv('Archives/olist_products_dataset.csv')

df_products.to_sql('products', engine, if_exists='replace', index=False)


# Lendo o arquivo "sellers" e adicionando no banco de dados
df_sellers = pd.read_csv('Archives/olist_sellers_dataset.csv')

df_sellers.to_sql('sellers', engine, if_exists='replace', index=False)


# Lendo o arquivo "product_category_name_translation" e adicionando no banco de dados
df_product_category_name_translation = pd.read_csv('Archives/product_category_name_translation.csv')

df_product_category_name_translation.to_sql('product_category_name_translation', engine, if_exists='replace', index=False)

