from extract import extraer_datos_carts,extraer_datos_productos,extraer_datos_usuarios
from transform import transformacion_Productos,transformacion_usuarios,transformacion_ventas
from load import load_dim_productos,load_dim_usuarios,load_fact_ventas
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()
usuario = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
base_datos = os.getenv("DB_NAME")

# 1. EXTRAER
productos = extraer_datos_productos()
usuarios = extraer_datos_usuarios()
carts = extraer_datos_carts()

# 2. TRANSFORMAR
df_productos = transformacion_Productos(productos)
df_usuarios = transformacion_usuarios(usuarios)
df_ventas = transformacion_ventas(carts)

# 3. CREAR ENGINE
engine = create_engine(f"postgresql://{usuario}:{password}@{host}:{puerto}/{base_datos}")

# 4. LOAD
load_dim_productos(df_productos, engine)
load_dim_usuarios(df_usuarios, engine)
load_fact_ventas(df_ventas, engine)
