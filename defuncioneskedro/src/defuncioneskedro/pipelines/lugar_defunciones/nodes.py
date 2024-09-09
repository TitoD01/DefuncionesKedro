"""
This is a boilerplate pipeline 'lugar_defunciones'
generated using Kedro 0.19.8
"""
import pandas as pd

def transformar_lugar_defuncion(df: pd.DataFrame) -> pd.DataFrame:
    """Transforma la columna LUGAR_DEFUNCION a enteros."""
    df['LUGAR_DEFUNCION'] = df['LUGAR_DEFUNCION'].map({
        'Casa habitación': 1,
        'Hospital o Clínica': 2,
        'Otro': 3
    })
    return df