use pyo3::prelude::*;

//~>
use crate::py_rs::snippet::pure_delete::discard_record;
use crate::py_rs::snippet::pure_insert::use_record;
use crate::py_rs::snippet::pure_read::{find_all, find_by_id, find_by_name, SnippetData};

//<·
#[pyclass]
pub struct SnippetDb;

#[pymethods]
impl SnippetDb {
    #[staticmethod]
    fn add_in(name: &str, version: &str, content: &str, _type: &str) -> PyResult<()> {
        let _ = use_record(name, version, content, _type)?;

        Ok(())
    }
    #[staticmethod]
    fn find_by_id(id: i32) -> PyResult<SnippetData> {
        let res = find_by_id(id)?;

        Ok(res)
    }
    #[staticmethod]
    fn find_by_name(name: &str) -> PyResult<SnippetData> {
        let res = find_by_name(name)?;

        Ok(res)
    }
    #[staticmethod]
    fn find_all() -> PyResult<Vec<SnippetData>> {
        let res = find_all()?;

        Ok(res)
    }
    #[staticmethod]
    fn discard(id: i32) -> PyResult<()> {
        let _ = discard_record(id)?;

        Ok(())
    }
}
