use diesel::prelude::*;
use pyo3::prelude::*;

use crate::db::establish_connection;
use crate::models::{NewProject, NewSnippet, Project, Snippet};
use crate::schema::{projects, snippets};

//<·
#[pyclass]
pub struct ProjectDb;

#[pymethods]
impl ProjectDb {
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

    #[staticmethod]
    fn add_in(
        composition: String,
        entrypoints: String,
        commands: String,

        version: String,
        langs: String,
        name: String,

        env: String,
    ) -> PyResult<i32> {
        let res = diesel::insert_into(projects::table)
            .values(&NewProject {
                composition: &composition,
                entrypoints: &entrypoints,
                commands: &commands,

                version: &version,
                langs: &langs,
                name: &name,

                env: &env,
            })
            .get_result::<Project>(&mut establish_connection())
            .map(|res| res.id);

        match res {
            Ok(id) => Ok(id),
            Err(e) => {
                eprintln!("Error inserting project: {:?}", e);
                Ok(0)
            }
        }


    }

    #[staticmethod]
    fn get_project(id: i32) -> PyResult<String> {
        Ok(projects::table
            .find(id)
            .select(Project::as_select())
            .first(&mut establish_connection())
            .ok()
            .and_then(|data| serde_json::to_string(&data).ok())
            .unwrap_or_default())
    }

    #[staticmethod]
    fn delete_project(id_: i32) -> PyResult<bool> {
        use crate::schema::projects::dsl::*;

        let res = diesel::delete(projects.filter(id.eq(id_)))
            .execute(&mut establish_connection())
            .unwrap_or(0);

        Ok(res > 0)
    }
}
