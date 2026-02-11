import pandas as pd
import streamlit as st

def pipeline_tratamento(caminho):
    df = ler_data(caminho)
    df = tratar_preco(df)
    df = criar_anuncio(df)
    df = criar_preco(df)
    df = remover_outlier_venda(df)
    df = tratar_area(df)
    df = tratar_cidade(df)
    df = to_numeric(df)
    return df


# Leitura do dataset
def ler_data(caminho):
    df = pd.read_csv(caminho, sep=';', header=0)
    return df


# Tratamento de preço
def tratar_preco(df):
    df["price"] = df["price"].str.replace('R\\$', '', regex=True).str.strip()
    df["price"] = df["price"].str.replace('.', '', regex=False)
    return df


# Classificação do tipo de anúncio
def criar_anuncio(df):
    df["tipo_anuncio"] = str('Vazio')
    df.loc[df["price"].str.contains("\n"), "tipo_anuncio"] = 'aluguel'
    df.loc[~df["price"].str.contains("\n"), "tipo_anuncio"] = 'venda'
    return df


# Criação do preço limpo
def criar_preco(df):
    df["price_limpo"] = df["price"]
    df["price_limpo"] = df["price_limpo"].str.replace(r"[^\d\s\.]", '', regex=True).str.strip()
    df["price_limpo"] = pd.to_numeric(df["price_limpo"])
    return df


# Remoção de outliers de venda
def remover_outlier_venda(df):
    outliers_venda = (df['price_limpo'] < 80000) & (df['tipo_anuncio'] == 'venda')
    df = df.drop(df[outliers_venda].index)
    return df


# Tratamento de área
def tratar_area(df):
    df["area_m2"] = df["area_m2"].str.replace('-', '', regex=True).str.strip()
    df["area_m2"] = pd.to_numeric(df["area_m2"])
    outliers_area = df["area_m2"] > 7500
    df = df.drop(df[outliers_area].index)
    return df


# Tratamento de cidade
def tratar_cidade(df):
    df["Cidade"] = df["Cidade"].fillna("São Paulo")
    return df


# Ajustes pontuais
def to_numeric(df):
    df = df.drop(columns="Unnamed: 0")
    df.loc[22, "quartos"] = 3
    df["quartos"] = pd.to_numeric(df["quartos"])
    df["banheiros"] = pd.to_numeric(df["banheiros"])
    df.loc[22, "vagas"] = 2
    df.loc[87, "vagas"] = 2
    df["vagas"] = pd.to_numeric(df["vagas"])
    return df
