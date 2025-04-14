use diesel::prelude::*;

#[derive(Queryable, Insertable, Copy, Clone)]
#[diesel(table_name = crate::schema::projects)]
pub struct Project {
    pub id: i32,
    pub entrypoints: String,
    pub commands: String,
    pub r#type: String,
    pub langs: String,
    pub name: String,
    pub env: String,
}

