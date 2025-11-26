
# Proyecto 2: Clasificación de Clientes con Clustering + KNN
# Autor: Iván Mendoza Ramos

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# 1. Crear dataset simulado
np.random.seed(42)
n_clientes = 300

ingresos = np.random.normal(50000, 15000, n_clientes)   # ingresos anuales
gasto = np.random.normal(5000, 2000, n_clientes)        # gasto en productos

df = pd.DataFrame({"ingresos": ingresos, "gasto": gasto})

# 2. Clustering con K-Means (segmentación)
kmeans = KMeans(n_clusters=3, random_state=42)
df["segmento"] = kmeans.fit_predict(df[["ingresos", "gasto"]])

# 3. Visualizar clusters
plt.figure(figsize=(8,6))
plt.scatter(df["ingresos"], df["gasto"], c=df["segmento"], cmap="viridis")
plt.xlabel("Ingresos Anuales")
plt.ylabel("Gasto en Productos")
plt.title("Segmentación de Clientes (K-Means)")
plt.show()

# 4. Clasificación con KNN
X = df[["ingresos", "gasto"]]
y = df["segmento"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 5. Evaluación del modelo
accuracy = knn.score(X_test, y_test)
print(f"Precisión del clasificador KNN: {accuracy*100:.2f}%")

# 6. Clasificar un nuevo cliente
nuevo_cliente = np.array([[60000, 7000]])  # ejemplo
segmento_pred = knn.predict(nuevo_cliente)
print(f"El nuevo cliente pertenece al segmento: {segmento_pred[0]}")

# Visualizar la predicción
plt.figure(figsize=(8,6))
plt.scatter(df["ingresos"], df["gasto"], c=df["segmento"], cmap="viridis", alpha=0.6)
plt.scatter(nuevo_cliente[0,0], nuevo_cliente[0,1], c="red", marker="X", s=200, label="Nuevo Cliente")
plt.xlabel("Ingresos Anuales")
plt.ylabel("Gasto en Productos")
plt.legend()
plt.title("Clasificación de Nuevo Cliente con KNN")
plt.show()      
