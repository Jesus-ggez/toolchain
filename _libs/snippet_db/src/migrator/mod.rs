use sea_orm::{ DatabaseConnection, DbErr };
use sea_orm_migration::prelude::*;

//·>
mod m20250404_000001_snippet;

//<·
pub struct Migrator;

#[async_trait::async_trait]
impl MigratorTrait for Migrator {
    fn migrations() -> Vec<Box<dyn MigrationTrait>> {
        vec![Box::new(m20250404_000001_snippet::Migration)]
    }
}

pub async fn init_database(db: DatabaseConnection) -> Result<(), DbErr> {
    let _schema_manager = SchemaManager::new(&db);
    Migrator::refresh(&db).await?;
    Ok(())
}
