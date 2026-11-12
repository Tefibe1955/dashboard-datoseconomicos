import pandas as pd
import requests
from datetime import datetime
import os

# 1. Obtener la fecha de hoy
fecha_hoy = datetime.now().strftime("%Y-%m-%d")

# 2. Extraer datos (Ejemplo: Dólar Blue usando DolarApi)
url = "https://dolarapi.com/v1/dolares/blue"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos_api = respuesta.json()
    dolar_compra = datos_api['compra']
    dolar_venta = datos_api['venta']
else:
    dolar_compra = None
    dolar_venta = None

# Aquí agregarías la recolección de las otras variables (Inflación, EMAE, etc.)
# ...

# 3. Crear el nuevo registro
nuevo_registro = {
    "Fecha": fecha_hoy,
    "Dolar_Blue_Compra": dolar_compra,
    "Dolar_Blue_Venta": dolar_venta
}

# 4. Guardar en el CSV
nombre_archivo = "datos_economicos.csv"

# Si el archivo ya existe, lo abrimos y le sumamos la fila
if os.path.exists(nombre_archivo):
    df_existente = pd.read_csv(nombre_archivo)
    # Convertimos el nuevo registro a un DataFrame temporal
    df_nuevo = pd.DataFrame([nuevo_registro])
    # Concatenamos y guardamos
    df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
else:
    # Si no existe (es la primera vez que corre), crea el archivo desde cero
    df_final = pd.DataFrame([nuevo_registro])

df_final.to_csv(nombre_archivo, index=False)
print(f"Datos guardados exitosamente para la fecha {fecha_hoy}")
