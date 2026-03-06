import streamlit as st
from src.processamento import pipeline_tratamento
from src.analise import (
    estatisticas_venda,
    estatisticas_preco_m2_venda,
    ranking_bairros_preco_m2
)
from src.visualizacao import (
    grafico_distribuicao_preco,
    grafico_distribuicao_preco_m2,
    grafico_ranking_bairros,
    grafico_area_vs_preco
)

# ========================
# PAGE CONFIG
# ========================

st.set_page_config(
    page_title="São Paulo Real Estate Dashboard",
    page_icon="🏙",
    layout="wide"
)

# ========================
# LOAD DATA
# ========================

caminho = "Dashboard_imobiliaria/data/analise_imoveis_sao_paulo.csv"
df = pipeline_tratamento(caminho)

# ========================
# SIDEBAR
# ========================

st.sidebar.title("Market Filters")

selected_neighborhood = st.sidebar.multiselect(
    "Neighborhood",
    options=df["Bairro"].unique(),
    default=df["Bairro"].unique()
)


price_range = st.sidebar.slider(
    "Price Range (R$)",
    int(df["price_limpo"].min()),
    int(df["price_limpo"].max()),
    (
        int(df["price_limpo"].min()),
        int(df["price_limpo"].max())
    )
)

top_n = st.sidebar.slider(
    "Top N Neighborhoods (Price per m²)",
    5, 20, 10
)

# ========================
# FILTERING
# ========================

filtered_df = df[
    (df["Bairro"].isin(selected_neighborhood)) &
    (df["price_limpo"].between(price_range[0], price_range[1]))
]


df_sales = filtered_df[
    filtered_df["tipo_anuncio"] == "venda"
]

# ========================
# STATISTICS
# ========================

stats_venda = estatisticas_venda(filtered_df)
stats_m2 = estatisticas_preco_m2_venda(filtered_df)
ranking = ranking_bairros_preco_m2(filtered_df, top_n=top_n)

# ========================
# HEADER
# ========================

st.title("Real Estate Intelligence Dashboard")
st.markdown("Strategic analysis of São Paulo's residential property market")

# ========================
# KPI SECTION
# ========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Sale Price", f"R$ {stats_venda['media']:,.0f}")
col2.metric("Median Sale Price", f"R$ {stats_venda['mediana']:,.0f}")
col3.metric("Average Price per m²", f"R$ {stats_m2['media']:,.0f}")
col4.metric("Total Listings", len(filtered_df))

st.markdown("---")

# ========================
# CHART LAYOUT (2x2)
# ========================

col_left, col_right = st.columns(2)

# ===== LEFT COLUMN =====
with col_left:

    st.subheader("Sales Price Distribution")

    with st.expander("Why this chart matters"):
        st.write("""
        This chart displays the distribution of property sale prices.
        It helps identify dominant price ranges and overall price dispersion.
        """)

    st.plotly_chart(
        grafico_distribuicao_preco(df_sales),
        use_container_width=True
    )

    st.subheader("Property Size vs. Sale Price")

    with st.expander("Why this chart matters"):
        st.write("""
        This scatter plot illustrates the relationship between property size and sale price,
        helping identify pricing inconsistencies and potential investment opportunities.
        """)

    st.plotly_chart(
        grafico_area_vs_preco(df_sales),
        use_container_width=True
    )

# ===== RIGHT COLUMN =====
with col_right:

    st.subheader("Price per Square Meter Distribution")

    with st.expander("Why this chart matters"):
        st.write("""
        Price per square meter standardizes property comparisons,
        offering clearer insight into relative market valuation.
        """)

    st.plotly_chart(
        grafico_distribuicao_preco_m2(df_sales),
        use_container_width=True
    )

    st.subheader("Neighborhood Ranking by Median Price per m²")

    with st.expander("Why this chart matters"):
        st.write("""
        This ranking highlights neighborhoods with the highest median price per square meter,
        serving as a strategic indicator of premium locations and high-value areas.
        """)

    st.plotly_chart(
        grafico_ranking_bairros(ranking),
        use_container_width=True
    )
st.sidebar.markdown("---")
st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.image(
    "Dashboard_imobiliaria/assets/logo.JPG", use_container_width=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
