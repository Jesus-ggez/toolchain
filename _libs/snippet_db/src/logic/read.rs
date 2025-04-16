use diesel::prelude::*;

use crate::models::Snippet;
use crate::schema::snippet::dsl::*;
use crate::db::establish_connection;

//<·

pub fn by_id(id_: i32) -> Result<String, Box<dyn std::error::Error>> {
    let data = snippet
        .find(id_)
        .select(Snippet::as_select())
        .first(&mut establish_connection())?;

    let json = serde_json::to_string(&data)?;

    Ok(json)
}

pub fn by_name(name_: &str) -> Result<String, Box<dyn std::error::Error>> {
    let data = snippet
        .filter(name.eq(name_))
        .load::<Snippet>(&mut establish_connection())?;

    let json = serde_json::to_string(&data)?;

    Ok(json)
}

pub fn all_records() -> Result<String, Box<dyn std::error::Error>> {
    let data: Vec<Snippet> = snippet
        .load(&mut establish_connection())?;

    let json = serde_json::to_string(&data)?;

    Ok(json)
}
