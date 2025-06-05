use diesel::prelude::*;
use pyo3::prelude::*;

use crate::class_py::SnippetDb;
use crate::db::establish_connection;
use crate::models::{NewSnippet, Snippet};
use crate::schema::snippets;

//<·
#[pymethods]
impl SnippetDb {
    #[staticmethod]
    fn set_snippet(name: String, content: String) -> PyResult<i32> {
        let res = diesel::insert_into(snippets::table)
            // struct { ... }
            .values(&NewSnippet {
                content: &content,
                name: &name,
            })
            .get_result::<Snippet>(&mut establish_connection())
            .map(|res| res.id);

        match res {
            Ok(id) => Ok(id),
            Err(e) => {
                eprintln!("Error inserting snippet: {:?}", e);
                Ok(0)
            }
        }
    }

    #[staticmethod]
    fn get_snippet(id: i32) -> PyResult<String> {
        Ok(snippets::table
            .find(id)
            .select(Snippet::as_select())
            .first(&mut establish_connection())
            .ok()
            .and_then(|data| serde_json::to_string(&data).ok())
            .unwrap_or_default())
    }

    #[staticmethod]
    fn delete_snippet(id_: i32) -> PyResult<bool> {
        use crate::schema::snippets::dsl::*;

        let res = diesel::delete(snippets.filter(id.eq(id_)))
            .execute(&mut establish_connection())
            .unwrap_or(0);

        Ok(res > 0)
    }
}
