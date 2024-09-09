"""
This is a boilerplate pipeline 'sexo_int'
generated using Kedro 0.19.8
"""
import pandas as pd


def transformar_glosa_sexo(df: pd.DataFrame) -> pd.DataFrame:
    df['GLOSA_SEXO'] = df['GLOSA_SEXO'].map({
        'Hombre': 1,
        'Mujer': 2,
        'Indeterminado': 3
    })
    return df