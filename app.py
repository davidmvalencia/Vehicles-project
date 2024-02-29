"""Venta de Autos - Aplicación Web con Casillas de Verificación"""
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # Leer los datos

st.header("Exploración de anuncios de vehículos en venta en Estados Unidos.")

# Casilla de verificación
build_histogram = st.checkbox('Visualización de los vehículos con histogramas.')

if build_histogram:
    st.write('Marcas y modelos de los autos disponibles en relación con su estado y kilometraje.')

    fig = px.histogram(car_data, x="model", y="odometer", color="condition",
                       color_discrete_map={"sedan": "blue", "suv": "green", "truck": "salmon"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=1000,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

if build_histogram:
    st.write('Cilindros de motor en relación con su tipo de vehículo y precio.')
    # Creamos un histograma basado en el número de cilindros de motor
    fig = px.histogram(car_data, x="cylinders", y="price", color="type",
                       color_discrete_map={"sedan": "blue", "suv": "green", "truck": "salmon"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=1000,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

# Botón de verificación
build_pie_chart_1 = st.button('Proporción de las condiciones de vehículos disponibles.')

if build_pie_chart_1:
    st.write('Porcentaje de las condiciones de los vehículos existentes.')
    # Creamos un diagrama de pastel basado en la condición con el precio
    fig = px.pie(car_data, values='price', names='condition')

    fig.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación
build_scatt = st.checkbox('Visualización de los vehículos con diagramas de dispersión.')

if build_scatt:
    st.write('Modelos por año de los vehículos en relación a su tipo y precio.')
    # Creamos un gráfico de dispersión basado en el año del modelo
    fig = px.scatter(car_data, x="model_year", y="price", color="type",
                     color_discrete_map={"sedan": "blue", "suv": "green", "truck": "gray"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=1000,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

if build_scatt:
    st.write('Kilometraje de los autos en relación a su condición y precio.')
    # Creamos un gráfico de dispersión basado en el kilometraje
    fig = px.scatter(car_data, x="odometer", y="price", color="condition",
                     color_discrete_map={"good": "blue", "like new": "green", "fair": "red"})
    # Ajustar el tamaño del gráfico
    fig.update_layout(
        autosize=False,
        width=1000,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)

 # Botón de verificación
build_pie_chart_2 = st.button('Proporción de los distintos tipos de vehículos disponibles.')

if build_pie_chart_2:
    st.write('Porcentaje de los tipos de vehículos existentes.')
    # Creamos un diagrama de pastel basado en la condición con el precio
    fig = px.pie(car_data, values='price', names='type')

    fig.update_traces(textposition='inside', textinfo='percent+label')

    fig.update_layout(
        autosize=False,
        width=1000,  # Ajustando el ancho según tus preferencias
        height=600)  # Ajustando la altura según tus preferencias

    st.plotly_chart(fig, use_container_width=True)
