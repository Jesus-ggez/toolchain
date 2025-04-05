use futures::executor::block_on;
use pyo3::types::PyDict;
use pyo3::prelude::*;
use sea_orm::*;

//~>
use crate::database::open_session;
use crate::entities::prelude::Snippet;
use crate::entities::snippet;

//<·
/// i dont know why I added the `to_dict` method
/// it exists for some reason so Ill just leave it as is
#[pyclass]
#[derive(Debug, Clone)]
pub struct SnippetData {
    #[pyo3(get)]
    pub id: i32,
    #[pyo3(get)]
    pub name: String,
    #[pyo3(get)]
    pub content: String,
    #[pyo3(get)]
    pub _type: String,
}

#[pymethods]
impl SnippetData {
    #[new]
    fn new(id: i32, name: String, content: String, _type: String) -> Self {
        SnippetData {
            content,
            _type,
            name,
            id,
        }
    }
    fn to_dict<'a>(&self, py: Python<'a>) -> PyResult<Bound<'a, PyDict>> {
        let dict = PyDict::new(py);
        dict.set_item("content", &self.content)?;
        dict.set_item("_type", &self._type)?;
        dict.set_item("name", &self.name)?;
        dict.set_item("id", self.id)?;
        Ok(dict)
    }
}

/*   ···   */
async fn op_async_id(id: i32) -> Result<SnippetData, DbErr> {
    let db = open_session().await?;
    let snippet = Snippet::find_by_id(id).one(&db).await?;

    match snippet {
        Some(snippet) => {
            if !snippet.active {
                return Err(DbErr::Custom("Snippet is inactive".to_string()));
            }

            Ok(SnippetData {
                id: snippet.id,
                name: snippet.name,
                content: snippet.content,
                _type: snippet.r#type,
            })
        }
        None => Err(DbErr::RecordNotFound(format!("Snippet not found"))),
    }
}

pub fn find_by_id(id: i32) -> PyResult<SnippetData> {
    match block_on(op_async_id(id)) {
        Ok(content) => Ok(content),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(
            e.to_string(),
        )),
    }
}

/*   ···   */
async fn op_async_name(name: &str) -> Result<Option<SnippetData>, DbErr> {
    let db = open_session().await?;
    let snippet = Snippet::find()
        .filter(snippet::Column::Name.eq(name))
        .one(&db)
        .await?;

    match snippet {
        Some(snippet) => {
            if !snippet.active {
                return Err(DbErr::Custom("Snippet is inactive".to_string()));
            }

            Ok(Some(SnippetData {
                id: snippet.id,
                name: snippet.name,
                content: snippet.content,
                _type: snippet.r#type,
            }))
        }
        None => Ok(None),
    }
}

pub fn find_by_name(name: &str) -> PyResult<SnippetData> {
    match block_on(op_async_name(name)) {
        Ok(Some(content)) => Ok(content),
        Ok(None) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Snippet not found",
        )),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(
            e.to_string(),
        ))?,
    }
}

/*   ···   */
async fn op_async_all() -> Result<Vec<SnippetData>, DbErr> {
    let db = open_session().await?;
    let snippets = Snippet::find()
        .filter(snippet::Column::Active.eq(true))
        .all(&db)
        .await?;

    Ok(snippets
        .into_iter()
        .map(|snippet| {
            if !snippet.active {
                return Err(DbErr::Custom("Found an inactive snippet".to_string()));
            }

            Ok(SnippetData {
                id: snippet.id,
                name: snippet.name,
                content: snippet.content,
                _type: snippet.r#type,
            })
        })
        .collect::<Result<Vec<_>, _>>()?)
}

pub fn find_all() -> PyResult<Vec<SnippetData>> {
    block_on(op_async_all())
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))
}
