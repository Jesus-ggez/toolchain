use pyo3::prelude::*;

use crate::logic;

//<·
#[pyclass]
pub struct SnippetDb;

#[pymethods]
impl SnippetDb {
    // create
    #[staticmethod]
    fn add_in(name: &str, version: &str, content: &str, _type: &str) -> PyResult<i32> {
        logic::create::add_single(name, version, content, _type)
            .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
    }

    // read
    #[staticmethod]
    fn find_by_id(id: i32) -> PyResult<String> {
        logic::read::by_id(id).map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
    }
    #[staticmethod]
    fn find_by_name(name: &str) -> PyResult<String> {
        logic::read::by_name(name)
            .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
    }
    #[staticmethod]
    fn find_all() -> PyResult<String> {
        logic::read::all_records()
            .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
    }

    // delete
    #[staticmethod]
    fn discard(id: i32) -> PyResult<()> {
        logic::delete::one(id).map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e.to_string()))
    }
}
