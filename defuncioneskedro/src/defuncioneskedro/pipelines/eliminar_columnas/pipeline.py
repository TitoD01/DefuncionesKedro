
from kedro.pipeline import Pipeline, node
from defuncioneskedro.pipelines.eliminar_columnas.nodes import eliminar_columnas

def create_pipeline(**kwargs) -> Pipeline:
    """Crea el pipeline para eliminar columnas."""
    return Pipeline(
        [
            node(
                func=eliminar_columnas,
                inputs="data_con_glosa_sexo_transformado",  
                outputs="data_sin_columnas", 
                name="eliminar_columnas_node",
            ),
        ]
    )



