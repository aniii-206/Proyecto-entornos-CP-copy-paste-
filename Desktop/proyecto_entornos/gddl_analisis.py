import pandas as pd
import numpy as np

def filtrar_expertos(df, enjoyment_min, song_name):
    """
    Filtra niveles con disfrute alto y una canción concreta.
    """
    return df[(df['Enjoyment'] > enjoyment_min) & (df['Song'] == song_name)]


def obtener_decimo_nivel(df):
    """
    Devuelve el décimo nivel ordenado por ID.
    """
    if len(df) < 10:
        return None
    return df.sort_values(by='ID').iloc[9]['Level Name']


def estadisticas_creador_top(df):
    """
    Analiza el creador con más niveles y sus niveles más/menos disfrutados.
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
    Niveles cuyo nombre coincide con la canción.
    """
    return df[df['Level Name'] == df['Song']]['Level Name'].tolist()


def verificar_coincidencia_disfrute(df):
    """
    Niveles donde dificultad (Tier) = disfrute.
    """
    return df[df['Tier'] == df['Enjoyment']]






def estadisticas_globales(df):
    return {
        'media': np.mean(df['Enjoyment']),
        'desviacion': np.std(df['Enjoyment'])
    }