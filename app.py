import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Recetas Saludables 5-Min 🥗",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Cargar los datos desde la ruta data/dataset.csv
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("./data/datos.csv",sep=';')
        df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos desde 'data/dataset.csv': {e}")
        return pd.DataFrame()

df = load_data()

# 2. Título y subtítulo llamativos con emojis
st.title("🥗 Fast & Fit: Panel de Control de Recetas Saludables en 5 Min ⏱️")
st.markdown(
    "### ⚡ *Analiza la interacción, nutrición y preferencias de los usuarios en tiempo real*"
)
st.markdown("---")

if not df.empty:
    # Barra lateral: Filtros Interactivos
    st.sidebar.header("🔍 Filtros de Interacción")

    # Filtro por Categoría
    categorias_disponibles = df["categoria"].unique().tolist()
    categorias_seleccionadas = st.sidebar.multiselect(
        "Categorías de Recetas:",
        options=categorias_disponibles,
        default=categorias_disponibles
    )

    # Filtro por Suscripción Premium
    tipo_suscripcion = st.sidebar.radio(
        "Tipo de Suscripción:",
        options=["Todas", "Solo Premium", "Solo Estándar"],
        index=0
    )

    # Filtro por Tiempo Máximo de Preparación
    max_tiempo = int(df["tiempo_preparacion_min"].max())
    min_tiempo = int(df["tiempo_preparacion_min"].min())
    tiempo_filtro = st.sidebar.slider(
        "Tiempo máx. de preparación (min):",
        min_value=min_tiempo,
        max_value=max_tiempo,
        value=max_tiempo
    )

    # Aplicación de Filtros al DataFrame
    df_filtered = df[
        (df["categoria"].isin(categorias_seleccionadas)) &
        (df["tiempo_preparacion_min"] <= tiempo_filtro)
    ]

    if tipo_suscripcion == "Solo Premium":
        df_filtered = df_filtered[df_filtered["suscripcion_premium"] == True]
    elif tipo_suscripcion == "Solo Estándar":
        df_filtered = df_filtered[df_filtered["suscripcion_premium"] == False]

    # Métricas Clave (KPIs)
    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    with col_kpi1:
        st.metric("Total Recetas Filtradas", len(df_filtered))
    with col_kpi2:
        avg_cal = df_filtered["calorias_kcal"].mean() if not df_filtered.empty else 0
        st.metric("Calorías Promedio", f"{avg_cal:.1f} kcal")
    with col_kpi3:
        avg_prot = df_filtered["proteina_g"].mean() if not df_filtered.empty else 0
        st.metric("Proteína Promedio", f"{avg_prot:.1f} g")
    with col_kpi4:
        avg_rating = df_filtered["valoracion_estrellas"].mean() if not df_filtered.empty else 0
        st.metric("Valoración Promedio", f"⭐ {avg_rating:.2f}")

    st.markdown("---")

    # 3. Checkbox para mostrar/ocultar vista previa del DataFrame
    if st.checkbox("📋 Mostrar / Ocultar vista previa interactiva del DataFrame"):
        st.subheader("👀 Vista Previa de Datos (Primeras 10 filas filtradas)")
        st.dataframe(
            df_filtered.head(10),
            use_container_width=True
        )

    st.markdown("### 📊 Métricas y Visualizaciones Interactivas")

    if not df_filtered.empty:
        # Layout de Gráficos (Columnas para uso eficiente del espacio)
        col1, col2 = st.columns(2)

        with col1:
            # Gráfico 1: Bar chart (Proteína promedio por categoría)
            df_cat = df_filtered.groupby("categoria")[["proteina_g", "calorias_kcal"]].mean().reset_index()
            fig_bar = px.bar(
                df_cat,
                x="categoria",
                y="proteina_g",
                color="categoria",
                text_auto=".1f",
                title="🥩 Proteína Promedio (g) por Categoría",
                labels={"categoria": "Categoría", "proteina_g": "Proteína (g)"},
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            fig_bar.update_layout(
                showlegend=False,
                xaxis_title="Categoría",
                yaxis_title="Proteína Promedio (g)",
                template="plotly_white"
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            # Gráfico 2: Donut Chart (Distribución de recetas por categoría)
            df_pie = df_filtered["categoria"].value_counts().reset_index()
            df_pie.columns = ["categoria", "cantidad"]
            fig_pie = px.pie(
                df_pie,
                names="categoria",
                values="cantidad",
                hole=0.4,
                title="🍰 Distribución de Recetas por Categoría",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig_pie.update_traces(textinfo="percent+label")
            fig_pie.update_layout(template="plotly_white")
            st.plotly_chart(fig_pie, use_container_width=True)

        # Gráfico 3: Histograma (Distribución de Valoración en Estrellas)
        st.markdown("---")
        fig_hist = px.histogram(
            df_filtered,
            x="valoracion_estrellas",
            color="suscripcion_premium",
            nbins=10,
            barmode="overlay",
            title="⭐ Distribución de Valoración en Estrellas (por Suscripción)",
            labels={
                "valoracion_estrellas": "Valoración (Estrellas)",
                "suscripcion_premium": "Suscripción Premium"
            },
            color_discrete_map={True: "#2ecc71", False: "#3498db"}
        )
        fig_hist.update_layout(
            xaxis_title="Valoración en Estrellas",
            yaxis_title="Cantidad de Recetas / Reseñas",
            template="plotly_white"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    else:
        st.warning("⚠️ No se encontraron datos para los filtros seleccionados.")
else:
    st.error("No se pudo cargar la base de datos. Verifica que exista el archivo 'data/dataset.csv'.")