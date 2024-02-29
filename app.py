"""Venta de Autos - Aplicación Web con Casillas de Verificación"""
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:\Users\David\Vehicles-project\vehicles_us.csv')

build_histogram = st.checkbox('Visualización con histogramas') # Casilla de verificación

if build_histogram:
    st.write('Marcas y modelos de los autos disponibles con relación a su estado y kilometraje.')
    # Areamos un histograma basado en el
    fig = px.histogram(car_data, x="model", y="odometer", color="condition",
                       color_discrete_map={"sedan": "blue", "suv": "green", "truck": "salmon"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=800,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

if build_histogram:
    st.write('Cilindros de motor con relación a su tipo de vehiculo y precio.')
    # Creamos un histograma basado en el numero de cilindros de motor
    fig = px.histogram(car_data, x="cylinders", y="price", color="type",
                       color_discrete_map={"sedan": "blue", "suv": "green", "truck": "salmon"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=800,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

build_scatt = st.checkbox('Visualización con diagramas de dispersion') # Casilla de verificacion

if build_scatt:
    st.write('Modelos por año de los vehiculos en relacion a su tipo y precio.')
    # Creamos un gráfico de dispersión basado en el año del modelo
    fig = px.scatter(car_data, x="model_year", y="price", color="type",
                     color_discrete_map={"sedan": "blue", "suv": "green", "truck": "black"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=800,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

if build_scatt:
    st.write('Kilometraje de los autos en relacion con su condicion y precio')
    # creamos un gráfico de dispersión basado en el kilometraje
    fig = px.scatter(car_data, x="odometer", y="price", color="condition",
                     color_discrete_map={"good": "blue", "like new": "green", "fair": "red"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=800,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)
