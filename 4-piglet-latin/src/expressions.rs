use std::fmt::Write;

use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

fn hello_world_str(output: &mut String) {
    write!(output, "Hello, World!").unwrap();
}

#[polars_expr(output_type=String)]
fn hello_world(inputs: &[Series]) -> PolarsResult<Series> {
    let ca = inputs[0].str()?;
    let out: StringChunked = ca.apply_into_string_amortized(|_value, output| {
        hello_world_str(output)
    });
    Ok(out.into_series())
}
