import requests 
import pandas as pd 
def extraer_datos_productos(): 
    url_products = "https://fakestoreapi.com/products" 
    respuesta_p = requests.get(url_products) 
    if respuesta_p.status_code != 200: 
        print("Ha ocurrido un error al cargar los datos") 
        
    datosP = respuesta_p.json() 
    return datosP 

def extraer_datos_usuarios(): 
    url_usuarios = "https://fakestoreapi.com/users" 
    respuesta_u = requests.get(url_usuarios) 
    if respuesta_u.status_code != 200: 
        print("Ha ocurrido un error al cargar los datos") 
    datosU = respuesta_u.json() 
    return datosU 

def extraer_datos_carts(): 
    url_carts = "https://fakestoreapi.com/carts" 
    respuesta_c = requests.get(url_carts) 
    if respuesta_c.status_code != 200: 
        print("Ha ocurrido un error al cargar los datos") 
    datosC = respuesta_c.json() 
    return datosC