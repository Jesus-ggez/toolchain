use futures::executor::block_on;
use pyo3::prelude::*;
use sea_orm::*;

//·>
use crate::config_db::open_session;
use crate::entities::prelude::Project;
use crate::entities::project;

//<
async fn op_async_discard(id: i32) -> Result<(), DbErr> {
    let db = open_session().await?;
    let project = Project::find_by_id(id)
        .one(&db)
        .await?
        .ok_or_else(|| DbErr::RecordNotFound(format!("Project with id {} not found", id)))?;
    let mut project_active: project::ActiveModel = project.into();

    project_active.active = ActiveValue::Set(false);
    project_active.update(&db).await?;

    Ok(())
}

pub fn discard_record(id: i32) -> PyResult<()> {
    block_on(op_async_discard(id))
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;

    Ok(())
}
