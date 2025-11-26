# Proyectos de Ciencia de Datos y Procesos ETL - Iván Mendoza Ramos

Este repositorio contiene dos proyectos de ciencia de datos y dos proyectos de ingeniería de datosrealizados en Python, que incluyen preparación de datos, análisis exploratorio, visualización y modelado predictivo. Todos los proyectos están diseñados para demostrar habilidades en análisis de datos, machine learning y visualización.

---
# Proyecto1_ETL_API_FAKESTORE: Integración de datos desde FakeStoreAPI hacia PostgreSQL

Desarrollé un pipeline ETL completo utilizando Python para extraer información de productos, 
usuarios y ventas desde la API pública FakeStoreAPI. 
Implementé un módulo de extracción con requests para recuperar 
los datos en formato JSON, seguido de un proceso de transformación 
donde estructuré, normalicé y limpié la información más relevante (
datos de productos, direcciones de usuarios y ventas generadas a partir de los carritos de compra).
Finalmente, construí un módulo de carga empleando SQLAlchemy para insertar los datos procesados en un modelo de Data Warehouse dentro de PostgreSQL,
utilizando tablas de dimensiones y una tabla de hechos. Las credenciales y la configuración de conexión se gestionan mediante variables de entorno (.env).
El proceso permite integrar los tres conjuntos de datos, generar DataFrames consistentes y almacenarlos en una base de datos de forma segura, flexible y escalable.

# Tecnologías
Python, Pandas, Requests, SQLAlchemy, PostgreSQL, dotenv

## Conceptos aplicados
ETL, APIs REST, JSON parsing, data cleaning, carga en base de datos, manejo de excepciones, diseño modular de pipelines.

---

## 1.Extracción (Extract)

El módulo de extracción obtiene la información desde tres endpoints de FakeStoreAPI:

- Products : productos del catálogo
- Users : usuarios registrados
- Carts : carritos que representan ventas
Cada función:
Realiza una solicitud HTTP con requests, valida el código de respuesta, devuelve los datos brutos en formato JSON como listas de diccionarios, esto permite desacoplar la extracción del resto del pipeline y reutilizarla en futuros procesos.

---
## 2. Transformación (Transform)

El módulo de transformación procesa cada conjunto de datos de manera independiente:

Transformación de productos
- Selecciona campos relevantes (id, nombre, precio, categoría).
- Construye un DataFrame limpio y estructurado.
- Reemplaza valores faltantes: media para columnas numéricas, 0 para columnas de texto

Transformación de usuarios
- Normaliza campos anidados (ciudad, código postal).
- Construye un DataFrame estructurado con identificador, username, email y dirección.
- Aplica reglas de limpieza y completado de valores.

Transformación de ventas (carts)
- Convierte cada carrito en varias filas de ventas individuales.
- Extrae productId, userId, quantity y fecha.
- Devuelve un DataFrame listo para nutrir la tabla de hechos.

Todo el proceso garantiza consistencia entre las dimensiones y la tabla fact.

---

## 3. Carga en PostgreSQL (Load)
 
El módulo de carga utiliza SQLAlchemy para:
- Conectarse al motor de PostgreSQL mediante un engine.
- Insertar los datos procesados en tres tablas: dim_productos2, dim_usuarios2, fact_ventas2
- Inserción fila por fila para asegurar control y manejo de excepciones.
- Lectura de credenciales desde .env.
- Este enfoque permite mantener las tablas actualizadas incluso si la API regresa nueva información.




---
# Proyecto2_ETL_API_REST_COUNTRIES: Integración de datos desde API RestCountries hacia PostgreSQL

Desarrollé un pipeline ETL completo utilizando Python para extraer información de países desde la API pública RestCountries. Implementé un módulo de extracción con requests para obtener datos en formato JSON, seguido de un proceso de transformación que estructuró y limpió la información (capital, región, población, idiomas, moneda y densidad poblacional). Finalmente, construí un módulo de carga empleando SQLAlchemy para insertar los datos procesados en una tabla dentro de una base de datos PostgreSQL, gestionando credenciales mediante variables de entorno (.env).
El proceso permite consultar múltiples países, generar un DataFrame consolidado y almacenarlo de forma segura y escalable.

## Tecnologías
Python, Pandas, Requests, SQLAlchemy, PostgreSQL, dotenv

## Conceptos aplicados
ETL, APIs REST, JSON parsing, data cleaning, carga en base de datos, manejo de excepciones, diseño modular de pipelines.

---

## 1. Extracción (Extract)

Se utiliza requests para realizar una consulta a la API:
- Recibe el nombre de un país.
- Valida el código de respuesta.
- Retorna los datos en formato JSON.

---

## 2. Transformación (Transform)

La función de transformación:
- Toma la respuesta JSON (lista con datos del país).
- Limpia y estructura los campos principales.
- Genera un diccionario con información como:
  - nombre común
  - capital
  - región / subregión
  - población
  - área
  - idiomas
  - moneda
  - densidad poblacional

También incluye una función para procesar múltiples países y devolver un DataFrame consolidado.

---

## 3. Carga en PostgreSQL (Load)

Se utiliza SQLAlchemy para:
- Crear la conexión a PostgreSQL.
- Cargar el DataFrame en la tabla especificada.
- Manejar credenciales mediante .env.

---

# Proyecto1_CienciaDeDatos: Clasificación de Clientes con Clustering + KNN**
- **Objetivo:** Segmentar clientes y clasificar nuevos clientes para mejorar estrategias de marketing y personalización de servicios.
- **Metodología:** 
  - Segmentación de clientes mediante **K-Means**.
  - Clasificación con **K-Nearest Neighbors (KNN)**.
  - Visualización de clusters y predicciones de nuevos clientes.
- **Tecnologías:** Python, Pandas, Numpy, Matplotlib, Scikit-Learn.

---

# Proyecto2_CienciaDeDatos: Predicción de Precios de Casas (Datos Reales)**
- **Objetivo:** Predecir precios de viviendas utilizando datos reales del dataset de Kaggle.
- **Metodología:** 
  - Limpieza y preparación completa de datos (valores faltantes, codificación de variables categóricas).
  - Modelo de regresión lineal para predicción de precios.
  - Evaluación con métricas MAE y RMSE.
  - Visualización de resultados y distribución de precios.
- **Tecnologías:** Python, Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn.
- **Dataset:** [House Prices: Advanced Regression Techniques (Kaggle)](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

---
