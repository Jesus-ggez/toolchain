use diesel::prelude::*;
use serde::{Serialize, Deserialize};

#[derive(Queryable, Selectable, Serialize, Deserialize, Debug, Clone)]
#[diesel(table_name = crate::schema::snippet)]
#[diesel(check_for_backend(diesel::sqlite::Sqlite))]
pub struct Snippet {
    pub id: i32,
    pub active: bool,
    pub version: String,
    pub content: String,
    pub type_: String,
    pub name: String,
}

#[derive(Insertable)]
#[diesel(table_name = crate::schema::snippet)]
pub struct NewSnippet<'a> {
    pub active: bool,
    pub version: &'a str,
    pub content: &'a str,
    pub type_: &'a str,
    pub name: &'a str,
}
