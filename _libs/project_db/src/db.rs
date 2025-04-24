use diesel::prelude::*;
use diesel::sqlite::SqliteConnection;
use dotenvy::dotenv;
use std::path::Path;
use std::env;

pub fn establish_connection() -> SqliteConnection {
    dotenv().ok();

    // env_db_url  || test.db
    let database_url = env::var("database_url").unwrap_or_else(|_| "test.db".to_string());

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
    create_tsnippets(&mut conn);
    create_tprojects(&mut conn);

    // implicit return
    conn
}
fn create_tsnippets(conn: &mut SqliteConnection) {
    diesel::sql_query(
        //name TEXT NOT NULL UNIQUE,
        r#"
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,
            content TEXT
        );
        "#,
    )
    .execute(conn)
    .expect("Failed to run migration");
}

fn create_tprojects(conn: &mut SqliteConnection) {
    diesel::sql_query(
        //name TEXT NOT NULL UNIQUE,
        r#"
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            composition TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL UNIQUE,
            version TEXT NOT NULL,
            langs TEXT NOT NULL,
            entrypoints TEXT,
            commands TEXT,
            env TEXT,
        );
        "#,
    )
    .execute(conn)
    .expect("Failed to run migration");
}

