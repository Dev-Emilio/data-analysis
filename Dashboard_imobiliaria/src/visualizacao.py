import matplotlib.pyplot as plt


def grafico_top_bairros_preco_m2(serie_ranking):
    serie_plot = serie_ranking.sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(serie_plot.index, serie_plot.values)

    ax.set_xlabel("Preço mediano por m² (R$)")
    ax.set_ylabel("Bairro")
    ax.set_title("Top bairros por preço mediano do m² (Venda)")

    plt.tight_layout()

    return fig