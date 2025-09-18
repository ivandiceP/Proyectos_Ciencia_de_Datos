# Proyecto 1: Predicción de Demanda de Inventario
# Autor: Iván Mendoza Ramos

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 1. Crear dataset simulado (ventas diarias durante 1 año)
np.random.seed(42)
dias = pd.date_range(start="2024-01-01", periods=365, freq="D")
ventas = 200 + 10*np.sin(np.linspace(0, 12*np.pi, 365)) + np.random.normal(0, 15, 365)

df = pd.DataFrame({"fecha": dias, "ventas": ventas})

# 2. Visualizar los datos
plt.figure(figsize=(12,5))
plt.plot(df["fecha"], df["ventas"], label="Ventas reales")
plt.title("Ventas diarias simuladas")
plt.xlabel("Fecha")
plt.ylabel("Unidades vendidas")
plt.legend()
plt.show()

# 3. Preparar datos para el modelo (regresión lineal con días como variable)
df["dia"] = np.arange(len(df))
X = df[["dia"]]
y = df["ventas"]

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test = X[:-73], X[-73:]
y_train, y_test = y[:-73], y[-73:]

# 4. Entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Predicciones
y_pred = modelo.predict(X_test)

# Evaluación
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Error MAE: {mae:.2f}")
print(f"Error RMSE: {rmse:.2f}")

# 6. Visualizar resultados
plt.figure(figsize=(12,5))
plt.plot(df["fecha"], y, label="Ventas reales")
plt.plot(df["fecha"].iloc[-73:], y_pred, color="red", label="Predicción (Regresión Lineal)")
plt.title("Predicción de Ventas con Regresión Lineal")
plt.xlabel("Fecha")
plt.ylabel("Unidades vendidas")
plt.legend()
plt.show()