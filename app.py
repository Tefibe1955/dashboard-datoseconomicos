import streamlit as st
import pandas as pd

# Título de la página
st.set_page_config(page_title="Dashboard Económico", layout="wide")
st.title("📊 Dashboard Económico: Nacional y Córdoba")

try:
    # Leer el archivo que genera tu robot
    df = pd.read_csv("datos_economicos.csv")
    
    # Mostrar una tabla con los últimos datos
    st.subheader("Últimos registros")
    st.dataframe(df.tail())

    # Crear un gráfico lineal simple para el Dólar Blue
    st.subheader("Evolución Dólar Blue")
    st.line_chart(data=df, x="Fecha", y=["Dolar_Blue_Compra", "Dolar_Blue_Venta"])

except FileNotFoundError:
    st.warning("El archivo de datos aún no se ha creado. Ve a la pestaña Actions y ejecuta el robot por primera vez.")
