use diesel::prelude::*;
use serde::{Deserialize, Serialize};
use crate::schema::{project, snippet};

//<·
#[derive(Queryable, Selectable, Serialize, Deserialize, Clone)]
#[diesel(table_name = snippet)]
#[diesel(check_for_backend(diesel::sqlite::Sqlite))]
pub struct Snippet {
    pub id: i32,
    pub content: String,
    pub name: String,
}

#[derive(Insertable)]
#[diesel(table_name = snippet)]
pub struct NewSnippet<'a> {
    pub content: &'a str,
    pub name: &'a str,
}

// Project
#[derive(Queryable, Selectable, Serialize, Deserialize, Clone)]
#[diesel(table_name = project)]
#[diesel(check_for_backend(diesel::sqlite::Sqlite))]
pub struct Project {
    pub id: i32,

    pub composition: String,
    pub entrypoints: String,
    pub commands: String,
    pub version: String,
    pub langs: String,
    pub name: String,
    pub env: String,
}

#[derive(Insertable)]
#[diesel(table_name = project)]
pub struct NewProject<'a> {
    pub composition: &'a str,
    pub entrypoints: &'a str,
    pub commands: &'a str,
    pub version: &'a str,
    pub langs: &'a str,
    pub name: &'a str,
    pub env: &'a str,
}
