use pyo3::prelude::*;

//~>
mod database;
mod entities;
mod identifier;
mod py_rs;

//·>
use identifier::Identifier;
use py_rs::prelude::*;

//<
#[pymodule]
fn snippet_db(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let _ = m.add_class::<Identifier>();
    let _ = m.add_class::<ProjectData>;
    let _ = m.add_class::<ProjectDb>;

    Ok(())
}
