use sea_orm::{DatabaseConnection, DbErr};
use sea_orm_migration::prelude::*;

//~>
mod m20250301_000001_snippet;
mod m20250301_000002_project;

//<
pub struct Migrator;

#[async_trait::async_trait]
impl MigratorTrait for Migrator {
    fn migrations() -> Vec<Box<dyn MigrationTrait>> {
        vec![
            //Box::new(m202503::Migration),
            Box::new(m20250301_000001_snippet::Migration),
            Box::new(m20250301_000002_project::Migration),
        ]
    }
}

pub async fn init_database(db: DatabaseConnection) -> Result<(), DbErr> {
    let _schema_manager = SchemaManager::new(&db);
    Migrator::refresh(&db).await?;
    Ok(())
}
