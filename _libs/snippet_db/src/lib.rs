use pyo3::prelude::*;

mod db;
mod logic;
mod main_py;
mod models;
mod schema;
mod identifier;

use identifier::Identifier;
use main_py::SnippetDb;

//<·
#[pymodule]
fn snippet_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<Identifier>()?;
    let _ = m.add_class::<SnippetDb>()?;
    Ok(())
}
