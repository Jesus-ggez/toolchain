use pyo3::prelude::*;

mod db;
mod main_py;
mod class_py;
mod models;
mod schema;

use crate::class_py::ProjectDb;


//<·
#[pymodule]
fn project_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<ProjectDb>()?;
    Ok(())
}
