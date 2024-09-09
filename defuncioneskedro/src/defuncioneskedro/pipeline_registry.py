"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from defuncioneskedro.pipelines.sexo_int.pipeline import create_pipeline as sexo_int
from defuncioneskedro.pipelines.lugar_defunciones.pipeline import create_pipeline as lugar_defunciones
from defuncioneskedro.pipelines.eliminar_columnas.pipeline import create_pipeline as eliminar_columnas


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["1"]= sexo_int()
    pipelines["2"]= lugar_defunciones()
    pipelines["3"] = eliminar_columnas()  # Registra el pipeline eliminar_columnas

    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
