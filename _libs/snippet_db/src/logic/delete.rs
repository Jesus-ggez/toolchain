use diesel::prelude::*;
use diesel::result::Error;

use crate::schema::snippet::dsl::*;
use crate::db::establish_connection;

//<·
pub fn one(id_: i32) -> Result<(), Error> {
    diesel::delete(snippet.filter(id.eq(id_)))
        .execute(&mut establish_connection())?;

    Ok(())
}
