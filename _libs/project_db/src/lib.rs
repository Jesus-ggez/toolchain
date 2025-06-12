use pyo3::prelude::*;

mod class_py;
mod db;
mod models;
mod py_project_table;
mod py_snippet_table;
mod py_tables;
mod schema;

use crate::class_py::{ProjectDb, SnippetDb};

//<·
#[pymodule]
fn project_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<ProjectDb>()?;
    let _ = m.add_class::<SnippetDb>()?;
    Ok(())
}
