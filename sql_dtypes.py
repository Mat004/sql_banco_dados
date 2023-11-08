import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Float

# Criando uma conexão com o banco de dados
engine = create_engine('sqlite:///banco_dados2.sqlite')

# Definindo o tipo de dados
df_customer_dtypes = {
    "customer_id"             :String(),                
    "customer_unique_id"      :String(),          
    "customer_zip_code_prefix":String(),     
    "customer_city"           :String(),               
    "customer_state"          :String()
}

# Lendo o arquivo "customers" e adicionando no banco de dados
df_customer = pd.read_csv('Archives/olist_customers_dataset.csv')
df_customer.to_sql('customers', engine, if_exists='replace', index=False, dtype=df_customer_dtypes)
