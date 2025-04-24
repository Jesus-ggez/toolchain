use pyo3::prelude::*;

mod db;
//mod logic;
mod main_py;
mod models;
mod schema;

use main_py::ProjectDb;

//<·
#[pymodule]
fn snippet_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<ProjectDb>()?;
    Ok(())
}
