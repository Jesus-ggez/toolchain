use pyo3::prelude::*;

mod db;
mod main_py;
mod models;
mod schema;

use main_py::ProjectDb;

//<·
#[pymodule]

fn project_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<ProjectDb>()?;
    Ok(())
}
