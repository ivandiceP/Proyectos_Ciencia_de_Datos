from PROCESO_EXTRACCION import extraer_datos
from PROCESO_TRANSFORMACION import transformacion
from PROCESO_TRANSFORMACION import procesar_varios_paises
from PROCESO_LOAD import cargar_df_postgres
import os
from dotenv import load_dotenv

paises = ["mexico", "canada" , "france","japan","argentina"]
datos_limpios = procesar_varios_paises(paises)
print(datos_limpios)
cargar_df_postgres(
    df=datos_limpios,
    nombre_tabla="ventas",
)

