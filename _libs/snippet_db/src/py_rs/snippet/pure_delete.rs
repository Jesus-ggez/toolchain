use futures::executor::block_on;
use pyo3::prelude::*;
use sea_orm::*;

//~>
use crate::database::open_session;
use crate::entities::prelude::Snippet;
use crate::entities::snippet;

//<·
async fn op_async_discard(id: i32) -> Result<(), DbErr> {
    let db = open_session().await?;
    let snippet = Snippet::find_by_id(id)
        .one(&db)
        .await?
        .ok_or_else(|| DbErr::RecordNotFound(format!("Snippet with id {} not found", id)))?;
    let mut snippet_active: snippet::ActiveModel = snippet.into();

    snippet_active.active = ActiveValue::Set(false);
    snippet_active.update(&db).await?;

    Ok(())
}

pub fn discard_record(id: i32) -> PyResult<()> {
    block_on(op_async_discard(id))
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;

    Ok(())
}
