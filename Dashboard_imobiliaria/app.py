import streamlit as st
from src.processamento import pipeline_tratamento
from src.analise import ranking_bairros_preco_m2
from src.visualizacao import grafico_top_bairros_preco_m2


st.title("Painel Imobiliario – São Paulo")

caminho = "data/analise_imoveis_sao_paulo.csv"

df = pipeline_tratamento(caminho)

ranking = ranking_bairros_preco_m2(df, top_n=10)

fig = grafico_top_bairros_preco_m2(ranking)

st.pyplot(fig)