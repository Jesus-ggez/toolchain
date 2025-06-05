use diesel::prelude::*;
use diesel::sqlite::SqliteConnection;
use dotenvy::dotenv;
use std::env;
use std::path::Path;

use crate::py_tables;

//<·
pub fn establish_connection() -> SqliteConnection {
    dotenv().ok();

    // var env
    let database_url = env::var("project_database_url").unwrap_or_else(|_| "test.db".to_string());

    // create_db
    if database_url.starts_with("sqlite:") || !database_url.contains("://") {
        let db_path = database_url.replace("sqlite:", "");
        if !Path::new(&db_path).exists() {
            std::fs::File::create(&db_path).expect("Failed to create Db file");
        }
    }

    // connection
    let mut conn = SqliteConnection::establish(&database_url)
        .unwrap_or_else(|_| panic!("Error connecting to {}", database_url));

    // run migrations
    py_tables::table_snippets(&mut conn);
    py_tables::table_projects(&mut conn);

    return conn;
}
