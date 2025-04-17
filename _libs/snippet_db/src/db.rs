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
