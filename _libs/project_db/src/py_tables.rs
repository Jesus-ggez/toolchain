use diesel::prelude::*;
use diesel::sqlite::SqliteConnection;


//<·
pub fn table_snippets(conn: &mut SqliteConnection) {
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

pub fn table_projects(conn: &mut SqliteConnection) {
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
            env TEXT
        );
        "#,
    )
    .execute(conn)
    .expect("Failed to run migration");
}
