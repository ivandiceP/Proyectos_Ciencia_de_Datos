from sqlalchemy import create_engine, text
import pandas as pd

# Cargar DIMENSION PRODUCTOS

def load_dim_productos(df, engine):
    """
    Esta función carga un DataFrame que contiene la información de una tabla de dimensiones y la carga a PostgreSQL
    
    Argumentos :
        df : df es un DataFrame, debe checarse que los nombres de las columnas del dataframe coincidan con los nombres 
             de la columna correspondiente de la tabla 
        engine : engine es la conexión con la cual te conectas a la base de datos correspondiente
    
    Retorna : Un mensaje donde notifica si la carga se realizó con exito o hubo algún error
    """
    try: 
        query = text("""
            INSERT INTO dim_productos2 (product_id, product_name, product_price, product_category)
            VALUES (:product_id, :product_name, :product_price, :product_category)
            ON CONFLICT (product_id)
            DO UPDATE SET 
                product_name = EXCLUDED.product_name,
                product_price = EXCLUDED.product_price,
                product_category = EXCLUDED.product_category;
        """)

        with engine.begin() as conn:
            for _, row in df.iterrows():
                conn.execute(query, row.to_dict())
        print("El DataFrame se ha cargado correctamente a la tabla de dimension dim_productos2")
    
    except:
        print("Ocurrió un error al cargar los datos en la tabla de dimension dim_productos2")



# Cargar DIMENSION USUARIOS

def load_dim_usuarios(df, engine):
    """
    Esta función carga un DataFrame que contiene la información de una tabla de dimensiones y la carga a PostgreSQL
    
    Argumentos :
        df : df es un DataFrame, debe checarse que los nombres de las columnas del dataframe coincidan con los nombres 
             de la columna correspondiente de la tabla 
        engine : engine es la conexión con la cual te conectas a la base de datos correspondiente
    
    Retorna : Un mensaje donde notifica si la carga se realizó con exito o hubo algún error
    """

    try: 
        query = text("""
            INSERT INTO dim_usuarios2 (usuario_id, username, email, city, zipcode)
            VALUES (:usuario_id, :username, :email, :city, :zipcode)
            ON CONFLICT (usuario_id)
            DO UPDATE SET
                username = EXCLUDED.username,
                email = EXCLUDED.email,
                city = EXCLUDED.city,
                zipcode = EXCLUDED.zipcode;
        """)

        with engine.begin() as conn:
            for _, row in df.iterrows():
                conn.execute(query, row.to_dict())
        print("El DataFrame se ha cargado correctamente a la de dimension tabla dim_usuario2")
    
    except:
        print("Ocurrió un error al cargar los datos en la tabla de dimension dim_usuarios2")


# Cargar FACT VENTAS (hechos)

def load_fact_ventas(df, engine):
    """
    Esta función carga un DataFrame que contiene la información de una tabla de dimensiones y la carga a PostgreSQL
    
    Argumentos :
        df : df es un DataFrame, debe checarse que los nombres de las columnas del dataframe coincidan con los nombres 
             de la columna correspondiente de la tabla 
        engine : engine es la conexión con la cual te conectas a la base de datos correspondiente
    
    Retorna : Un mensaje donde notifica si la carga se realizó con exito o hubo algún error
    """

    try:
        query = text("""
            INSERT INTO fact_ventas2 (id_venta, product_id, usuario_id, date, quantity)
            VALUES (:id_venta, :product_id, :usuario_id, :date, :quantity)
            ON CONFLICT (id_venta, product_id, usuario_id)
            DO NOTHING;
        """)

        with engine.begin() as conn:
            for _, row in df.iterrows():
                conn.execute(query, row.to_dict())
        print("El DataFrame se ha cargado correctamente a la tabla de hechos fact_ventas2")

    except:
        print("Ocurrió un error al cargar los datos en la tabla de hechos fact_ventas2")
