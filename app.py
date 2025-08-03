import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')
 
# Título principal
st.title("🚗 Análisis Interactivo de Vehículos Usados")

st.markdown("Explora visualmente el conjunto de datos con histogramas y gráficos de dispersión usando botones interactivos.")

# Botón para construir histograma
if st.button("📊 Construir histograma de kilometraje"):
    st.write("✅ Creando histograma de la columna `odometer` (kilometraje)...")

    fig_hist = px.histogram(
        car_data.dropna(subset=["odometer"]),
        x="odometer",
        nbins=50,
        title="Distribución del Kilometraje de Vehículos Usados",
        labels={"odometer": "Kilometraje (millas)"},
        color_discrete_sequence=["#636EFA"],
        opacity=0.8
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button("📈 Construir gráfico de dispersión (odometer vs price)"):
    st.write("✅ Creando gráfico de dispersión para `odometer` y `price`...")

    fig_scatter = px.scatter(
        car_data.dropna(subset=["odometer", "price"]),
        x="odometer",
        y="price",
        color="condition",
        title="Relación entre Kilometraje y Precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)", "condition": "Condición"},
        opacity=0.6,
        color_discrete_sequence=px.colors.qualitative.Set1,
        hover_data=["model", "model_year", "type"]
    )
    st.plotly_chart(fig_scatter, use_container_width=True)