use pyo3::prelude::*;

#[pyfunction]
fn greet_me() -> PyResult<String> {
    Ok("Hello, world!".to_string())
}

#[pymodule]
fn hello_world(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(greet_me, m)?)?;
    Ok(())
}
