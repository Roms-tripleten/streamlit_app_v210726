# 🥗 Fast & Fit Analytics: Dashboard Interactivo de Recetas en 5 Minutos ⏱️

> *"Transformando datos de nutrición exprés en insights accionables mediante visualizaciones interactivas de alto impacto."*

---

## 📌 Descripción del Proyecto

**Fast & Fit Analytics** es una aplicación web interactiva desarrollada para analizar el comportamiento, las preferencias culinarias y las métricas nutricionales de los usuarios de una plataforma de recetas saludables preparadas en **5 minutos o menos**.

A través de un enfoque basado en **Data-Driven Decision Making**, este panel de control permite examinar cómo se distribuye el consumo por categoría, evaluar el aporte proteico por platillo y analizar la percepción de satisfacción del usuario según su tipo de suscripción (*Premium vs. Estándar*).

### ✨ Características Principales
* 📊 **Métricas Nutricionales en Tiempo Real:** Cálculo dinámico de calorías, proteínas y valoraciones promedio.
* 🎛️ **Filtros Multidimensionales:** Segmentación inteligente por categoría de alimentos, tiempo de preparación y modalidad de suscripción.
* 📈 **Visualizaciones Interactivas de Plotly:** Gráficos responsivos de barras, distribución circular (donut) e histogramas de valoración.
* 📋 **Explorador de Datos:** Vista previa interactiva de los datos subyacentes con actualización dinámica en función de los filtros aplicados.

---

## 🛠️ Tecnologías Utilizadas

El proyecto utiliza un *stack* moderno de Python optimizado para ciencia de datos y desarrollo *frontend* dinámico:

* 🐍 **[Python 3.10+](https://www.python.org/):** Lenguaje principal para la manipulación y procesamiento de datos.
* 📊 **[Pandas](https://pandas.pydata.org/):** Limpieza, estructuración y filtrado del conjunto de datos.
* 🚀 **[Streamlit](https://streamlit.io/):** Framework para el desarrollo ágil de la interfaz de usuario interactiva.
* 🎨 **[Plotly Express](https://plotly.com/python/plotly-express/):** Motor de gráficos vectoriales interactivos.

---

## 💻 Instrucciones de Instalación y Ejecución Local

Sigue estos pasos simples para ejecutar el panel interactivo en tu entorno local:

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/fast-and-fit-analytics.git
cd fast-and-fit-analytics
```

### 2. Crear y Activar un Entorno Virtual (Recomendado)
* **En macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **En Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Instalar Dependencias
Asegúrate de instalar las bibliotecas requeridas especificadas en el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

> **Contenido de `requirements.txt`:**
> ```text
> streamlit>=1.30.0
> pandas>=2.0.0
> plotly>=5.18.0
> ```

### 4. Ejecutar la Aplicación
Lanza la aplicación de Streamlit desde la terminal:
```bash
streamlit run app.py
```

La aplicación estará disponible automáticamente en tu navegador web local en la dirección: `http://localhost:8501`.

---

## 📂 Estructura del Proyecto

```text
fast-and-fit-analytics/
├── data/
│   └── dataset.csv          # Conjunto de datos sintético (separado por ;)
├── app.py                   # Código principal de la aplicación en Streamlit
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del proyecto
```

---

## 📬 Contacto y Contribuciones

¡Las contribuciones y sugerencias son siempre bienvenidas! Si tienes alguna idea para mejorar las métricas o añadir nuevas funciones:

1. Haz un **Fork** del repositorio.
2. Crea una rama con tu nueva función (`git checkout -b feature/NuevaFuncion`).
3. Envía tus cambios mediante un **Pull Request**.

---

*Desarrollado con 💚 para impulsar un estilo de vida saludable y basado en datos.*