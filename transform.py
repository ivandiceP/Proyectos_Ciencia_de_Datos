import pandas as pd 

def transformacion_Productos(datosP):
    """
    Esta función transforma una lista de diccionarios con productos en un DataFrame limpio y con valores faltantes reemplazados.

    Argumentos:
        datosP: lista de diccionarios que contienen datos de productos.
    Retorna:
        Un DataFrame con la transformación realizada.
    """
    
    datos_transformados = []
    # Seleccionamos los datos que queremos obtener del diccionario
    for p in datosP:
        datos_transformados.append({
            "product_id": p.get("id"),
            "product_name": p.get("title"),
            "product_price": p.get("price"),
            "product_category": p.get("category")
        })

    dfP = pd.DataFrame(datos_transformados)

    # Llenar faltantes (media para numéricas, 0 para no numéricas)
    valores_reemplazo = {}
    for col in dfP.columns:
        if dfP[col].dtype != 'object':          # Si es numérica
            media = dfP[col].mean()
            valores_reemplazo[col] = media if not pd.isna(media) else 0
        else:                                   # Si es texto/categoría
            valores_reemplazo[col] = 0

    dfP = dfP.fillna(valores_reemplazo)

    return dfP



def transformacion_usuarios(datosU): 
    """
    Esta función transforma una lista de diccionarios con productos en un DataFrame limpio y con valores faltantes reemplazados.

    Argumentos:
        datosU: lista de diccionarios que contienen datos de los usuarios.
    Retorna:
        Un DataFrame con la transformación realizada.
    """
    datos_transformados = [] 
    for u in datosU: 
        datos_transformados_usuarios = { 
            "usuario_id" : u["id"], 
            "username" : u["username"], 
            "email" : u["email"], 
            "city" : u["address"]["city"], 
            "zipcode" : u["address"]["zipcode"] 
            } 
        datos_transformados.append(datos_transformados_usuarios) 

    dfu = pd.DataFrame(datos_transformados) 

    # Llenar faltantes (media para numéricas, 0 para no numéricas)
    valores_reemplazo = {}
    for col in dfu.columns:
        if dfu[col].dtype != 'object':          # Si es numérica
            media = dfu[col].mean()
            valores_reemplazo[col] = media if not pd.isna(media) else 0
        else:                                   # Si es texto/categoría
            valores_reemplazo[col] = 0

    dfu = dfu.fillna(valores_reemplazo)
    return dfu 



def transformacion_ventas(datosC): 
    """
    Esta función transforma una lista de diccionarios con productos en un DataFrame limpio y con valores faltantes reemplazados.

    Argumentos:
        datosC: lista de diccionarios que contienen datos de las carts.
    Retorna:
        Un DataFrame con la transformación realizada.
    """
    datos_transformados = [] 
    for c in datosC: 
        cart_id = c["id"] 
        user_id = c["userId"] 
        date = c["date"] 
        # Cada producto del carrito es una venta 
        for p in c["products"]: 
            venta = { 
                    "id_venta": cart_id, 
                    "product_id": p["productId"], 
                     "usuario_id": user_id, 
                     "date": date, 
                     "quantity": p["quantity"], 
                     } 
        datos_transformados.append(venta) 

    df_fact = pd.DataFrame(datos_transformados) 

    # Llenar faltantes (media para numéricas, 0 para no numéricas)
    valores_reemplazo = {}
    for col in df_fact.columns:
        if df_fact[col].dtype != 'object':          # Si es numérica
            media = df_fact[col].mean()
            valores_reemplazo[col] = media if not pd.isna(media) else 0
        else:                                   # Si es texto/categoría
            valores_reemplazo[col] = 0

    df_fact = df_fact.fillna(valores_reemplazo)
    return df_fact