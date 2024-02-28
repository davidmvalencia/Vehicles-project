"""Venta de Autos - Aplicación Web con Casillas de Verificación"""
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:/Users/David/Vehicles-project/vehicles_us.csv')

build_histogram = st.checkbox('Construir un histograma') # crea una casilla de verificación

if build_histogram:
    st.write('Tipo de autos disponibles en venta')

    fig = px.histogram(car_data, x="type")

    st.plotly_chart(fig, use_container_width=True)

build_scatt = st.checkbox('Construir diagrama de dispersion') # crea una casilla de verificacion

if build_scatt:
    st.write('Precio de los autos acorde al modelo disponible')

    fig = px.scatter(car_data, x="model", y="price")

    st.plotly_chart(fig, use_container_width=True)
