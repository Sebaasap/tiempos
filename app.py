
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("Tiempo_espera.csv")


tab1, tab2 = st.tabs(["Análisis Univariado", "Análisis Bivariado"])


with tab1:
    st.header("Análisis Univariado de Tiempo de Espera")

    st.subheader("Histograma general")
    st.plotly_chart(px.histogram(df, x='Tiempo_espera_min'))

    st.subheader("Frecuencia por Estación")
    st.dataframe(df['Estacion'].value_counts())
    st.plotly_chart(px.histogram(df, x='Estacion', y='Tiempo_espera_min'))

    st.subheader("Frecuencia por Hora")
    st.dataframe(df['Hora'].value_counts())
    st.plotly_chart(px.histogram(df, x='Hora', y='Tiempo_espera_min'))

    st.subheader("Frecuencia por Puntualidad")
    st.dataframe(df['Puntual'].value_counts())
    st.plotly_chart(px.histogram(df, x='Puntual', y='Tiempo_espera_min'))

    st.subheader("Frecuencia por Clima")
    st.dataframe(df['Clima'].value_counts())
    st.plotly_chart(px.histogram(df, x='Clima', y='Tiempo_espera_min'))

    st.subheader("Frecuencia por Demanda Alta")
    st.dataframe(df['Demanda_alta'].value_counts())
    st.plotly_chart(px.histogram(df, x='Demanda_alta', y='Tiempo_espera_min'))

    st.subheader("Frecuencia por Hora Pico")
    st.dataframe(df['Es_hora_pico'].value_counts())
    st.plotly_chart(px.histogram(df, x='Es_hora_pico', y='Tiempo_espera_min'))


with tab2:
    st.header("Análisis Bivariado de Tiempo de Espera")

    st.subheader("Boxplot: Estación vs Tiempo de Espera")
    st.plotly_chart(px.box(df, x='Estacion', y='Tiempo_espera_min'))

    st.subheader("Clima vs Tiempo de Espera")
    st.plotly_chart(px.box(df, x='Clima', y='Tiempo_espera_min'))

    st.subheader("Hora vs Tiempo de Espera")
    st.plotly_chart(px.box(df, x='Hora', y='Tiempo_espera_min'))

    st.subheader("Puntualidad vs Tiempo de Espera")
    st.plotly_chart(px.box(df, x='Puntual', y='Tiempo_espera_min'))

    st.subheader("Demanda Alta vs Tiempo de Espera")
    st.plotly_chart(px.box(df, x='Demanda_alta', y='Tiempo_espera_min'))

    st.subheader("Hora Pico vs Tiempo de Espera")
    st.plotly_chart(px.box(df, x='Es_hora_pico', y='Tiempo_espera_min'))
