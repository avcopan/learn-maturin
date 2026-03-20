import polars as pl
from expression_lib import language

df = pl.DataFrame(
    {
        "names": ["Richard", "Alice", "Bob"],
    }
)

out = df.with_columns(
    greeting=language.hello_world("names"),
)

print(out)
