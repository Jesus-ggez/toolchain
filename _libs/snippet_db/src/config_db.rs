use dotenvy::dotenv;
use sea_orm::*;
use std::env;

const DB_NAME: &str = "code";

pub async fn open_session() -> Result<DatabaseConnection, DbErr> {
    let _ = dotenv();
    let database_url: &str =
        &env::var("DATABASE_URL").unwrap_or_else(|_| "sqlite::memory:".to_string());

    let test: &str = &env::var("TEST_MODE").unwrap_or_else(|_| "false".to_string());
    if test == "true" {
        dbg!("{}", database_url);
    }

    let db: DatabaseConnection = Database::connect(database_url).await?;
    let db = &match db.get_database_backend() {
        DbBackend::MySql => {
            db.execute(Statement::from_string(
                db.get_database_backend(),
                format!("CREATE DATABASE IF NOT EXISTS `{}`;", DB_NAME),
            ))
            .await?;

            let url = format!("{}/{}", database_url, DB_NAME);
            Database::connect(&url).await?
        }
        DbBackend::Postgres => {
            db.execute(Statement::from_string(
                db.get_database_backend(),
                format!("DROP DATABASE IF EXISTS \"{}\";", DB_NAME),
            ))
            .await?;
            db.execute(Statement::from_string(
                db.get_database_backend(),
                format!("CREATE DATABASE \"{}\";", DB_NAME),
            ))
            .await?;

            let url = format!("{}/{}", database_url, DB_NAME);
            Database::connect(&url).await?
        }
        DbBackend::Sqlite => db,
    };

    Ok(db.clone())
}
