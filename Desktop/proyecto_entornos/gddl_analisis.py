"""
Módulo de Análisis Estadístico para Geometry Dash Demon List (GDDL).

Este script proporciona herramientas para analizar la relación entre la dificultad, 
el disfrute de los usuarios y la música en niveles de Geometry Dash.
"""

import pandas as pd
import numpy as np

def filtrar_expertos(df, enjoyment_min, song_name):
    """
    Filtra niveles que superan un umbral de disfrute y usan una canción específica.

    Args:
        df (pd.DataFrame): Dataset con la información de los niveles.
        enjoyment_min (float): Valor mínimo de disfrute (0-10).
        song_name (str): Nombre de la canción a filtrar.

    Returns:
        pd.DataFrame: Un subconjunto del dataframe original con los niveles filtrados.
    """
    return df[(df['Enjoyment'] > enjoyment_min) & (df['Song'] == song_name)]


def obtener_decimo_nivel(df):
    """
    Ordena los niveles por su ID y extrae el nombre del que ocupa la décima posición.

    Args:
        df (pd.DataFrame): Dataset con la información de los niveles.

    Returns:
        str: Nombre del nivel en la posición 10 o None si hay menos de 10 registros.
    """
    if len(df) < 10:
        return None
    return df.sort_values(by='ID').iloc[9]['Level Name']


def estadisticas_creador_top(df):
    """
    Identifica al creador más prolífico y analiza la calidad de sus obras.

    Busca quién tiene más niveles registrados y determina cuál es su nivel
    con mayor y menor puntuación de disfrute.

    Args:
        df (pd.DataFrame): Dataset con la información de los niveles.

    Returns:
        dict: Diccionario con el nombre del creador, su nivel más popular, 
              el menos popular y el promedio de disfrute.
    """
    creador = df['Creator'].value_counts().idxmax()
    subset = df[df['Creator'] == creador]

    return {
        'nombre': creador,
        'mas_popular': subset.loc[subset['Enjoyment'].idxmax(), 'Level Name'],
        'menos_popular': subset.loc[subset['Enjoyment'].idxmin(), 'Level Name'],
        'media_disfrute': subset['Enjoyment'].mean()
    }


def niveles_homonimos(df):
    """
    Encuentra niveles que comparten el mismo nombre que su canción.

    Returns:
        list: Lista de strings con los nombres de los niveles encontrados.
    """
    return df[df['Level Name'] == df['Song']]['Level Name'].tolist()


def verificar_coincidencia_disfrute(df):
    """
    Detecta niveles donde el valor de dificultad (Tier) coincide exactamente 
    con la puntuación de disfrute.

    Args:
        df (pd.DataFrame): Dataset con la información de los niveles.

    Returns:
        pd.DataFrame: Filtrado de niveles con Tier igual a Enjoyment.
    """
    return df[df['Tier'] == df['Enjoyment']]


def estadisticas_globales(df):
    """
    Calcula las métricas descriptivas generales del disfrute en el dataset.

    Args:
        df (pd.DataFrame): Dataset con la información de los niveles.

    Returns:
        dict: Diccionario con la 'media' y la 'desviacion' estándar del disfrute.
    """
    return {
        'media': np.mean(df['Enjoyment']),
        'desviacion': np.std(df['Enjoyment'])
    }