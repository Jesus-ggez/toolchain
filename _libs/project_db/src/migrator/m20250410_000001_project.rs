use sea_orm_migration::prelude::*;

pub struct Migration;

impl MigrationName for Migration {
    fn name(&self) -> &str {
        "m20250410_000001_project"
    }
}

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        manager
            .create_table(
                Table::create()
                    .table(Project::Table)
                    .col(
                        ColumnDef::new(Project::Id)
                            .integer()
                            .not_null()
                            .auto_increment()
                            .primary_key(),
                    )
                    //.col(ColumnDef::new(Project::).string().not_null())
                    .col(ColumnDef::new(Project::Entrypoints).string())
                    .col(ColumnDef::new(Project::Commands).string())
                    .col(ColumnDef::new(Project::VarEnvs).string())
                    .col(ColumnDef::new(Project::Langs).string().not_null())
                    .col(
                        ColumnDef::new(Project::Content)
                            .string()
                            .not_null()
                            .unique_key(),
                    )
                    .col(ColumnDef::new(Project::Version).string().not_null())
                    .col(ColumnDef::new(Project::Active).boolean().not_null())
                    .col(
                        ColumnDef::new(Project::Name)
                            .string()
                            .not_null()
                            .unique_key(),
                    )
                    .col(ColumnDef::new(Project::Type).string().not_null())
                    .to_owned(),
            )
            .await
    }

    async fn down(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        manager
            .drop_table(Table::drop().table(Project::Table).to_owned())
            .await
    }
}

#[derive(Iden)]
pub enum Project {
    Table,
    Id,

    //<
    Entrypoints,
    Commands,
    VarEnvs,
    Content,
    Version,
    Active,
    Langs,
    Name,
    Type,
}
