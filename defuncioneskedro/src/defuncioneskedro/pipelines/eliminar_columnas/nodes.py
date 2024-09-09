import pandas as pd

def eliminar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina columnas específicas del DataFrame."""
    columnas_a_eliminar = [
        'DIAG2',
        'CAPITULO_DIAG2',
        'GLOSA_CAPITULO_DIAG2',
        'CODIGO_GRUPO_DIAG2',
        'GLOSA_GRUPO_DIAG2',
        'CODIGO_CATEGORIA_DIAG2',
        'GLOSA_CATEGORIA_DIAG2',
        'CODIGO_SUBCATEGORIA_DIAG2',
        'GLOSA_SUBCATEGORIA_DIAG2'
    ]
    return df.drop(columns=columnas_a_eliminar, axis=1, errors='ignore')


