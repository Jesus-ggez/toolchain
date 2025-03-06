use futures::executor::block_on;
use pyo3::prelude::*;
use sea_orm::*;

//·>
use crate::config_db::open_session;
use crate::entities::prelude::Project;
use crate::entities::project;

//<
async fn op_async(
    // ...
    name: String,
    version: String,
    composition: String,
) -> Result<(), DbErr> {
    let record = project::ActiveModel {
        name: ActiveValue::Set(name),
        version: ActiveValue::Set(version),
        composition: ActiveValue::Set(composition),
        active: ActiveValue::Set(true),
        ..Default::default()
    };

    let db = open_session().await?;
    let txn = db.begin().await?;

    Project::insert(record).exec(&txn).await?;
    txn.commit().await?;
    Ok(())
}

pub fn use_record(name: &str, version: &str, composition: &str) -> PyResult<()> {
    let name = name.to_owned();
    let version = version.to_owned();
    let composition = composition.to_owned();

    block_on(op_async(name, version, composition))
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;

    Ok(())
}
