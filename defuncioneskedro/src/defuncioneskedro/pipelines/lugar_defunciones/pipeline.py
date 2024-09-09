"""
This is a boilerplate pipeline 'lugar_defunciones'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import transformar_lugar_defuncion


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=transformar_lugar_defuncion,
                inputs="data_con_glosa_sexo_transformado",  # Ajusta esto a tu entrada real
                outputs="lugar_defunciones",  # Ajusta esto a tu salida real
                name="transformar_lugar_defuncion_node"
            ),])
