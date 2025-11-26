from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Cargar variables del .env una sola vez
load_dotenv()

def cargar_df_postgres(df,nombre_tabla,if_exists="append"):
    """
    Esta función lo que hace es cargar la consulta de la lista de países a una tabla en la base de datos "mi_base_etl" de PostgreSQL
    Argumentos: 
        df : Es el nombre que tiene el dataframe cuando mandas a llamar a la función procesar_varios_paises 
        nombre_tabla : Es el nombre de la tabla con el que quieres guardar tus datos en la base de datos
    Retorna: Un mensaje que confirma si la carga se dio correctamente o hubo algún error
    """

    # Cargar variables del entorno dentro de la función
    usuario = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    puerto = os.getenv("DB_PORT")
    base_datos = os.getenv("DB_NAME")

    # Validación para detectar si faltan variables
    if None in [usuario, password, host, puerto, base_datos]:
        print("Error: Algunas variables del .env no se cargaron.")
        print("Valores leídos:")
        print("DB_USER:", usuario)
        print("DB_PASSWORD:", password)
        print("DB_HOST:", host)
        print("DB_PORT:", puerto)
        print("DB_NAME:", base_datos)
        return

    try:
        engine = create_engine(
            f"postgresql+psycopg2://{usuario}:{password}@{host}:{puerto}/{base_datos}"
        )

        print("Conexión creada correctamente")

        with engine.begin() as connection:
            df.to_sql(
                name=nombre_tabla,
                con=connection,
                if_exists=if_exists,
                index=False
            )

        print(f"DataFrame cargado en la tabla '{nombre_tabla}'")

    except Exception as e:
        print("Error:", e)
