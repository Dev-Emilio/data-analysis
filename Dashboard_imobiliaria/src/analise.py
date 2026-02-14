import numpy as np


def estatisticas_venda(df):
    vendas = df.loc[df["tipo_anuncio"] == "venda", "price_limpo"].dropna().to_numpy()

    return {
        "media": np.mean(vendas),
        "mediana": np.median(vendas),
        "desvio_padrao": np.std(vendas),
        "minimo": np.min(vendas),
        "maximo": np.max(vendas),
    }


def estatisticas_preco_m2_venda(df):
    preco_m2 = df.loc[df["tipo_anuncio"] == "venda", "preco_m2"].dropna().to_numpy()

    return {
        "media": np.mean(preco_m2),
        "mediana": np.median(preco_m2),
        "desvio_padrao": np.std(preco_m2),
        "minimo": np.min(preco_m2),
        "maximo": np.max(preco_m2),
    }


def ranking_bairros_preco_m2(df, top_n=10):
    mediana = (
        df.groupby("Bairro")["preco_m2"]
        .median()
        .dropna()
        .sort_values(ascending=False)
        .head(top_n)
    )

    return mediana
