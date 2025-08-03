import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')
 
 # Título de la sección
st.header("📊 Exploración del Kilometraje de Vehículos Usados")

# Casilla para habilitar el histograma
build_histogram = st.checkbox("Mostrar opciones para construir un histograma")

if build_histogram:
    st.markdown("Selecciona la opción para construir un histograma interactivo del kilometraje (`odometer`).")

    # Botón para construir el histograma
    if st.button("🔨 Construir histograma"):
        st.success("✅ Histograma creado para la columna `odometer` del conjunto de datos.")

        # Crear histograma con mejor estilo
        fig = px.histogram(
            car_data.dropna(subset=["odometer"]),
            x="odometer",
            nbins=50,
            title="Distribución del Kilometraje de Vehículos Usados",
            labels={"odometer": "Kilometraje (millas)"},
            color_discrete_sequence=["#636EFA"],
            opacity=0.8
        )

        # Estilo del layout
        fig.update_layout(
            title_font_size=20,
            xaxis_title_font_size=16,
            yaxis_title_font_size=16,
            plot_bgcolor="#f9f9f9",
            paper_bgcolor="#ffffff"
        )

        # Mostrar el gráfico
        st.plotly_chart(fig, use_container_width=True)