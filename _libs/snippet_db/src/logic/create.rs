use diesel::prelude::*;
use diesel::result::Error;

use crate::schema::snippet;
use crate::models::{NewSnippet, Snippet};
use crate::db::establish_connection;

//<·
pub fn add_single(name: &str, version: &str, content: &str, _type: &str) -> Result<i32, Error> {
    let record = NewSnippet {
        version: version,
        content: content,
        active: true,
        type_: _type,
        name: name,
    };

    let snippet: Snippet = diesel::insert_into(snippet::table)
        .values(&record)
        .get_result(&mut establish_connection())?;

    Ok(snippet.id)
}


