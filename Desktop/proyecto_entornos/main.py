import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import gddl_analisis as gddl

# -------------------
# 📥 CARGA DE DATOS
# -------------------
try:
    df = pd.read_csv(r'C:\Users\Diego\Desktop\proyecto_entornos\gddl_dataset.csv')
except FileNotFoundError:
    df = pd.read_csv('gddl_dataset.csv')

df.columns = df.columns.str.strip()

print("✅ Dataset cargado correctamente.")

# -------------------
# 🔍 PROCESAMIENTO
# -------------------
res1 = gddl.filtrar_expertos(df, 7, "Theory of everything 2")
res2 = gddl.estadisticas_creador_top(df)
correlacion = gddl.correlacion_dificultad_disfrute(df)
media = gddl.media_disfrute_por_dificultad(df)
stats = gddl.estadisticas_globales(df)

# -------------------
# 📊 GRÁFICAS CORREGIDAS
# -------------------
print("\nGenerando gráficas mejoradas...")

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6) # Un poco más ancho para mejorar legibilidad

# 1. Distribución de dificultad (CORRECCIÓN: USAMOS HISTOGRAMA)
plt.figure()
# Usamos histplot en lugar de countplot para evitar el manchón negro en el eje X
sns.histplot(data=df, x='Tier', bins=30, kde=True, color="#440154") 
plt.title('Distribución de Niveles por Dificultad (Tier)', fontsize=14)
plt.xlabel('Dificultad (Tier)')
plt.ylabel('Frecuencia (Cantidad de niveles)')
plt.savefig('barras.png', dpi=300)

# 2. Dificultad vs Disfrute
plt.figure()
sns.scatterplot(data=df, x='Tier', y='Enjoyment', alpha=0.3, color="#3498db", s=20)
sns.regplot(data=df, x='Tier', y='Enjoyment', scatter=False, color="red", line_kws={"linewidth":2})
plt.title('Relación: Dificultad vs Disfrute', fontsize=14)
plt.savefig('scatter.png', dpi=300)

# 3. Disfrute medio por dificultad
plt.figure()
sns.lineplot(x=media.index, y=media.values, marker='o', color='#2ecc71', linewidth=2)
plt.fill_between(media.index, media.values, alpha=0.2, color='#2ecc71')
plt.title('Tendencia de Disfrute Medio por Tier', fontsize=14)
plt.savefig('linea.png', dpi=300)

# 4. Histograma de Disfrute
plt.figure()
sns.histplot(df['Enjoyment'], kde=True, color="#9b59b6", bins=15)
plt.title('Distribución de Puntuaciones de Disfrute', fontsize=14)
plt.savefig('histograma.png', dpi=300)

plt.close('all')
print("✅ Gráficas guardadas. Revisa 'barras.png' ahora, debería ser legible.")

# -------------------
# 🌐 INTERACTIVA
# -------------------
fig = px.scatter(
    df,
    x="Tier",
    y="Enjoyment",
    color="Creator",
    hover_name="Level Name",
    title="Análisis GDDL Interactivo",
    template="plotly_white"
)
fig.write_html("interactivo.html")