use diesel::prelude::*;
use pyo3::prelude::*;

use crate::class_py::ProjectDb;
use crate::db::establish_connection;
use crate::models::{NewProject, Project};
use crate::schema::projects;

//<·
#[pymethods]
impl ProjectDb {
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
    fn get_by_id(id: i32) -> PyResult<String> {
        Ok(projects::table
            .find(id)
            .select(Project::as_select())
            .first(&mut establish_connection())
            .ok()
            .and_then(|data| serde_json::to_string(&data).ok())
            .unwrap_or_default())
    }

    #[staticmethod]
    fn get_by_name(name_: String) -> PyResult<String> {
        use crate::schema::projects::dsl::*;

        Ok(projects
            .filter(name.eq(name_))
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
