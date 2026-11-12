import pandas as pd
import requests
from datetime import datetime
import os

# 1. Obtener la fecha de hoy
fecha_hoy = datetime.now().strftime("%Y-%m-%d")

# --- EXTRACCIÓN DE DATOS ---

# A. Dólar Blue (DolarApi)
try:
    url_dolar = "https://dolarapi.com/v1/dolares/blue"
    datos_dolar = requests.get(url_dolar).json()
    dolar_venta = datos_dolar['venta']
except:
    dolar_venta = None

# B. Variables Nacionales (API Oficial de Datos Argentina)
# Usamos los IDs del INDEC: IPC General y Actividad (EMAE)
try:
    url_nacional = "https://apis.datos.gob.ar/series/api/series/?ids=148.3_INDEC_IPC_NACION_M_0_22,143.3_NO_PR_2004_A_21&limit=1&format=json"
    datos_nacional = requests.get(url_nacional).json()['data'][0]
    
    # La API devuelve una lista: [Fecha original, valor IPC, valor EMAE]
    ipc_nacional = datos_nacional[1]
    emae_nacional = datos_nacional[2]
except:
    ipc_nacional = None
    emae_nacional = None

# C. Variables de Córdoba
# Dejamos la estructura lista. Requiere Web Scraping avanzado.
ipc_cordoba = None

# --- GUARDADO DE DATOS ---

# 3. Crear el nuevo registro agrupando todo
nuevo_registro = {
    "Fecha": fecha_hoy,
    "Dolar_Blue_Venta": dolar_venta,
    "IPC_Nacional": ipc_nacional,
    "EMAE_Nacional": emae_nacional,
    "IPC_Cordoba": ipc_cordoba
}

nombre_archivo = "datos_economicos.csv"

# 4. Guardar en el CSV (Pandas agregará las columnas nuevas automáticamente)
if os.path.exists(nombre_archivo):
    df_existente = pd.read_csv(nombre_archivo)
    df_nuevo = pd.DataFrame([nuevo_registro])
    df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
else:
    df_final = pd.DataFrame([nuevo_registro])

df_final.to_csv(nombre_archivo, index=False)
print(f"Datos guardados exitosamente para la fecha {fecha_hoy}")
