use pyo3::prelude::*;

//·>
use crate::py_rs::project::pure_delete::discard_record;
use crate::py_rs::project::pure_insert::use_record;
use crate::py_rs::project::pure_read::{find_all, find_by_id, find_by_name, ProjectData};

//<
#[pyclass]
pub struct ProjectDb;

#[pymethods]
impl ProjectDb {
    #[staticmethod]
    fn add_in(name: &str, version: &str, composition: &str) -> PyResult<()> {
        let _ = use_record(name, version, composition)?;

        Ok(())
    }
    #[staticmethod]
    fn find_by_id(id: i32) -> PyResult<ProjectData> {
        let res = find_by_id(id)?;

        Ok(res)
    }
    #[staticmethod]
    fn find_by_name(name: &str) -> PyResult<ProjectData> {
        let res = find_by_name(name)?;

        Ok(res)
    }
    #[staticmethod]
    fn find_all() -> PyResult<Vec<ProjectData>> {
        let res = find_all()?;

        Ok(res)
    }
    #[staticmethod]
    fn discard(id: i32) -> PyResult<()> {
        let _ = discard_record(id)?;

        Ok(())
    }
}
