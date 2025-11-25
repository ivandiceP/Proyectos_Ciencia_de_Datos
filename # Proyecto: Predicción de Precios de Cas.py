# Proyecto: Predicción de Precios de Casas (Housing Prices) - Datos reales
# Autor: Iván Mendoza Ramos

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Cargar dataset
df = pd.read_csv("train.csv")  # asegúrate de tener train.csv descargado de Kaggle

# 2. Separar variable objetivo
y = df["SalePrice"]
X = df.drop("SalePrice", axis=1)

# 3. Codificar variables categóricas
X = pd.get_dummies(X, drop_first=True)

# 4. Imputar valores faltantes
X = X.fillna(X.mean())

# 5. División entrenamiento/prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Entrenar modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Predicciones
y_pred = model.predict(X_test)

# 8. Evaluación
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")

# 9. Visualización resultados
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Precios Reales")
plt.ylabel("Precios Predichos")
plt.title("Predicción de Precios de Casas - Regresión Lineal")
plt.show()

# 10. Análisis exploratorio rápido
plt.figure(figsize=(10,6))
sns.histplot(df['SalePrice'], kde=True)
plt.title("Distribución de Precios de Casas")
plt.xlabel("Precio de Venta")
plt.show()