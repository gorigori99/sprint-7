import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us (1).csv') 

# Crear un botón en Streamlit
hist_button = st.button('Construir histograma') 

if hist_button:  # al hacer clic en el botón
    # Escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
        fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button('construir diagrama de dispersion')
if scatter_button: 
    # Escribir otro mensaje para el gráfico de dispersión
        st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
        fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig_scatter, use_container_width=True)