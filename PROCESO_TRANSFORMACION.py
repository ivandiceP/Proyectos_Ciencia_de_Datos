from PROCESO_EXTRACCION import extraer_datos
import pandas as pd

def transformacion(datos):
    """
    Transforma los datos extraídos en un formato estructurado, especificamente en un diccionario
    Argumentos:
        datos :  datos debe ser un diccionario para que la función pueda funcionar correctamente
    Retorna : Un diccionario con los 9 pares clave-valor definidas en la función.
    """
    if datos is None:
        return None
    
    pais = datos[0]  # agarramos 0 ya que la API regresa una lista

    datos_transformados = {
        "pais": pais["name"]["common"],
        "capital": pais["capital"][0] if "capital" in pais else None,
        "region": pais["region"],
        "subregion": pais["subregion"],
        "poblacion": pais["population"],
        "area": pais["area"],
        "idiomas": ", ".join(pais["languages"].values()),
        "moneda": list(pais["currencies"].keys())[0],
        "densidad_poblacional": pais["population"] / pais["area"] if pais.get("population") and pais.get("area") else None #ya que no podemos dividir entre 0
    }

    return datos_transformados



def procesar_varios_paises(lista_paises):
    """
    Obtiene el diccionario de cada país a consultar, a la cual los convierte en un DataFrame
    Argumentos:
        lista_paises : lista_paises debe ser un diccionario que contiene los paises a consultar
    Retorna: Retorna un DataFrame con toda la información de cada país.
    """
    resultados = []

    for pais in lista_paises:
        datos = extraer_datos(pais)
        datos_limpios = transformacion(datos)

        if datos_limpios:
            resultados.append(datos_limpios)

    df_final = pd.DataFrame(resultados)
    return df_final
