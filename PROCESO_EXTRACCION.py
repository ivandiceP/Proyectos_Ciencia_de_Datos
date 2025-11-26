import pandas as pd
import requests


def extraer_datos(pais):
    """
    Esta funcion extrae los datos del API de Rest Countries 
    Argumentos:
        pais : recibe el nombre del pais que quierers consultar

    Retorna: Un diccionario en formato JSON con los datos del país consultado
    """
    url = f"https://restcountries.com/v3.1/name/{pais}"
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print("No se puede cargar la solicitud API")
    
    datos = respuesta.json()
    return datos

