use futures::executor::block_on;
use sea_orm::*;

//~>
mod config_db;
mod migrator;

//·>
use config_db::open_session;
use migrator::init_database;

//<
async fn run() -> Result<(), DbErr> {
    let _db: DatabaseConnection = open_session().await?;

    init_database(_db.clone()).await?;

    Ok(())
}

fn main() {
    if let Err(err) = block_on(run()) {
        panic!("{}", err)
    }
}
