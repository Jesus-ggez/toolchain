use futures::executor::block_on;
use pyo3::prelude::*;
use sea_orm::*;

//·>
use crate::config_db::open_session;
use crate::entities::prelude::Project;
use crate::entities::project;

//<
#[pyclass]
#[derive(Debug, Clone)]
pub struct ProjectData {
    #[pyo3(get)]
    pub id: i32,
    #[pyo3(get)]
    pub name: String,
    #[pyo3(get)]
    pub composition: String,
}

/*   ···   */
async fn op_async_id(id: i32) -> Result<ProjectData, DbErr> {
    let db = open_session().await?;
    let project = Project::find_by_id(id).one(&db).await?;

    match project {
        Some(project) => {
            if !project.active {
                return Err(DbErr::Custom("Project is inactive".to_string()));
            }

            Ok(ProjectData {
                id: project.id,
                name: project.name,
                composition: project.composition,
            })
        }
        None => Err(DbErr::RecordNotFound(format!("Project not found"))),
    }
}

pub fn find_by_id(id: i32) -> PyResult<ProjectData> {
    match block_on(op_async_id(id)) {
        Ok(composition) => Ok(composition),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(
            e.to_string(),
        )),
    }
}

/*   ···   */
async fn op_async_name(name: &str) -> Result<Option<ProjectData>, DbErr> {
    let db = open_session().await?;
    let project = Project::find()
        .filter(project::Column::Name.eq(name))
        .one(&db)
        .await?;

    match project {
        Some(project) => {
            if !project.active {
                return Err(DbErr::Custom("Project is inactive".to_string()));
            }

            Ok(Some(ProjectData {
                id: project.id,
                name: project.name,
                composition: project.composition,
            }))
        }
        None => Ok(None),
    }
}

pub fn find_by_name(name: &str) -> PyResult<ProjectData> {
    match block_on(op_async_name(name)) {
        Ok(Some(composition)) => Ok(composition),
        Ok(None) => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Project not found",
        )),
        Err(e) => Err(PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(
            e.to_string(),
        ))?,
    }
}

/*   ···   */
async fn op_async_all() -> Result<Vec<ProjectData>, DbErr> {
    let db = open_session().await?;
    let projects = Project::find()
        .filter(project::Column::Active.eq(true))
        .all(&db)
        .await?;

    Ok(projects
        .into_iter()
        .map(|project| {
            if !project.active {
                return Err(DbErr::Custom("Found an inactive project".to_string()));
            }

            Ok(ProjectData{
                id: project.id,
                name: project.name,
                composition: project.composition,
            })
        })
        .collect::<Result<Vec<_>, _>>()?)
}

pub fn find_all() -> PyResult<Vec<ProjectData>> {
    block_on(op_async_all())
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))
}
