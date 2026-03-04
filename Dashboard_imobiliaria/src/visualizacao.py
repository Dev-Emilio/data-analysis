import plotly.express as px


def grafico_distribuicao_preco(df_vendas):
    fig = px.histogram(
        df_vendas,
        x="price_limpo",
        nbins=40
    )

    fig.update_layout(
        height=450,
        xaxis_title="Price (R$)",
        yaxis_title="Amount"
    )

    return fig


def grafico_distribuicao_preco_m2(df_vendas):
    fig = px.histogram(
        df_vendas,
        x="preco_m2",
        nbins=40
    )

    fig.update_layout(
        height=450,
        xaxis_title="Price per m²",
        yaxis_title="Amount"
    )

    return fig


def grafico_ranking_bairros(ranking_series):
    df_rank = ranking_series.reset_index()
    df_rank.columns = ["Neighborhood", "price m²"]

    fig = px.bar(
        df_rank,
        x="price m²",
        y="Neighborhood",
        orientation="h"
    )

    fig.update_layout(
        height=500,
        xaxis_title="Median per m²",
        yaxis_title="Neighborhood"
    )

    return fig


def grafico_area_vs_preco(df_vendas):
    fig = px.scatter(
        df_vendas,
        x="area_m2",
        y="price_limpo"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Area (m²)",
        yaxis_title="Price (R$)"
    )

    return fig