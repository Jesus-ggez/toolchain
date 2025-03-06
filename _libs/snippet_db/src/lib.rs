use pyo3::prelude::*;

//~>
mod config_db;
mod entities;
mod py_rs;

//·>
use py_rs::prelude::*;


//<
#[cfg_attr(not(debug_assertions), allow(unused_macros))]

#[pymodule]
fn snippet_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<SnippetDb>();
    let _ = m.add_class::<ProjectDb>();

    Ok(())
}
