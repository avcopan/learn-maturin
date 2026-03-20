from __future__ import annotations

from typing import TYPE_CHECKING
from pathlib import Path

import polars as pl
from polars.plugins import register_plugin_function

if TYPE_CHECKING:
    from typing import TypeAlias

    import polars as pl

    IntoExprColumn: TypeAlias = pl.Expr | str | pl.Series

PLUGIN_PATH = Path(__file__).parent

def hello_world(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        plugin_path=PLUGIN_PATH,
        args=[expr],
        function_name="hello_world",
        is_elementwise=True,
    )
