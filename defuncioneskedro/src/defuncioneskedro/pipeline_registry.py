"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from defuncioneskedro.pipelines.sexo_int.pipeline import create_pipeline as sexo_int
from defuncioneskedro.pipelines.lugar_defunciones.pipeline import create_pipeline as lugar_defunciones


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["1"]= sexo_int()
    pipelines["2"]= lugar_defunciones()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
