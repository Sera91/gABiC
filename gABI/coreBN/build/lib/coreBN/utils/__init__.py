from .mathext import cartesian, sample_discrete
from .state_name import StateNameMixin
from .check_functions import _check_1d_array_object, _check_length_equal
from .optimizer import optimize, pinverse
from .utils import get_example_model
from .GAMfit import GAM_residuals, GAM_residuals_fast


__all__ = [
    "cartesian",
    "sample_discrete",
    "StateNameMixin",
    "_check_1d_array_object",
    "_check_length_equal",
    "optimize",
    "pinverse",
    "get_example_model",
    "GAM_residuals",
    "GAM_residuals_fast"
]
