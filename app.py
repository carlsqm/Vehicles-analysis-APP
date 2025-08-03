import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')
 
# Título
st.title("🚗 Análisis Interactivo de Vehículos Usados")
st.markdown("Filtra los datos por año y condición antes de generar visualizaciones interactivas.")

# ---------------------- FILTROS ----------------------
# Eliminar filas con model_year o condition vacíos
filtered_data = car_data.dropna(subset=["model_year", "condition"])

# Filtro por rango de año
min_year = int(filtered_data["model_year"].min())
max_year = int(filtered_data["model_year"].max())
year_range = st.slider("📅 Selecciona el rango de años", min_year, max_year, (min_year, max_year))

# Filtro por condición (checkbox múltiple)
available_conditions = sorted(filtered_data["condition"].dropna().unique())
selected_conditions = st.multiselect("🚘 Elige condiciones del vehículo", available_conditions, default=available_conditions)

# Aplicar filtros
filtered_data = filtered_data[
    (filtered_data["model_year"] >= year_range[0]) &
    (filtered_data["model_year"] <= year_range[1]) &
    (filtered_data["condition"].isin(selected_conditions))
]

# ---------------------- BOTÓN HISTOGRAMA ----------------------
if st.button("📊 Construir histograma de kilometraje"):
    st.write("✅ Histograma de `odometer` para vehículos filtrados")
    fig_hist = px.histogram(
        filtered_data.dropna(subset=["odometer"]),
        x="odometer",
        nbins=50,
        title="Distribución del Kilometraje",
        labels={"odometer": "Kilometraje (millas)"},
        color_discrete_sequence=["#636EFA"],
        opacity=0.8
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# ---------------------- BOTÓN DISPERSIÓN ----------------------
if st.button("📈 Construir gráfico de dispersión (odometer vs price)"):
    st.write("✅ Gráfico de dispersión `odometer` vs `price` para vehículos filtrados")
    fig_scatter = px.scatter(
        filtered_data.dropna(subset=["odometer", "price"]),
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