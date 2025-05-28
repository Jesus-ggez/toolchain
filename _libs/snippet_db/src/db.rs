use diesel::prelude::*;
use diesel::sqlite::SqliteConnection;
use dotenvy::dotenv;
use std::env;
use std::path::Path;

pub fn establish_connection() -> SqliteConnection {
    dotenv().ok();

    // var env
    let database_url = env::var("snippet_database_url").unwrap_or_else(|_| "test.db".to_string());
    let test = env::var("test").unwrap_or_else(|_| "false".to_string());

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

    // test
    if test == "true" {
        reset_db(&mut conn);
    }

    // run migrations
    run_migrations(&mut conn);

    // implicit return
    conn
}

fn run_migrations(conn: &mut SqliteConnection) {
    diesel::sql_query(
        r#"
        CREATE TABLE IF NOT EXISTS snippet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            version TEXT NOT NULL,
            content TEXT UNIQUE,
            type_ TEXT NOT NULL,
            active INTEGER
        );
        "#,
    )
    .execute(conn)
    .expect("Failed to run migration");
}

fn reset_db(conn: &mut SqliteConnection) {
    use crate::schema::snippet::dsl::*;

    diesel::delete(snippet)
        .execute(conn)
        .expect("failed deleting db");
}
