import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_excel('BaseFuncionarios.xlsx')

def contagem(coluna):
    contagem = df[coluna].value_counts().reset_index()
    contagem.columns = [coluna, 'Contagem']
    return contagem

def grafico(coluna):
    fig = px.bar(contagem(coluna), x = coluna, y = 'Contagem', title = f'Contagem de profissionais por {coluna}', text_auto = True)
    fig.update_layout(width = int(width))

    return fig

st.set_page_config(layout = 'wide')

width = st.slider('Escolha o tamanho do gráfico:', min_value = 400, max_value = 800, value = 400)

st.title('Dashboard de RH')
st.text('Este dashboard faz uma análise exploratória da base de RH')

col1, col2 = st.columns([1, 1])

col1.plotly_chart(grafico('Cargo'))
col2.plotly_chart(grafico('Genero'))

st.sidebar.title('Opções')