use futures::executor::block_on;
use pyo3::prelude::*;
use sea_orm::*;

//~>
use crate::database::open_session;
use crate::entities::prelude::Snippet;
use crate::entities::snippet;

//<·
async fn op_async(
    name: String,
    version: String,
    content: String,
    _type: String,
) -> Result<(), DbErr> {
    let record = snippet::ActiveModel {
        name: ActiveValue::Set(name),
        version: ActiveValue::Set(version),
        content: ActiveValue::Set(content),
        active: ActiveValue::Set(true),
        r#type: ActiveValue::Set(_type),
        ..Default::default()
    };

    let db = open_session().await?;
    let txn = db.begin().await?;
    
    Snippet::insert(record).exec(&txn).await?;
    txn.commit().await?;
    Ok(())
}

pub fn use_record(name: &str, version: &str, content: &str, _type: &str) -> PyResult<()> {
    let name = name.to_owned();
    let version = version.to_owned();
    let content = content.to_owned();
    let _type = _type.to_owned();

    block_on(op_async(name, version, content, _type))
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;

    Ok(())
}
