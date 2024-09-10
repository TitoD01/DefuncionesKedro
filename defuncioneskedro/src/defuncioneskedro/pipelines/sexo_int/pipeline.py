"""
This is a boilerplate pipeline 'sexo_int'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import transformar_glosa_sexo


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([            
            node(
                func=transformar_glosa_sexo,
                inputs="defunciones",  
                outputs="data_con_glosa_sexo_transformado", 
                name="transformar_glosa_sexo_node"
            ),])
