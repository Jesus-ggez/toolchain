use sea_orm_migration::prelude::*;

pub struct Migration;

impl MigrationName for Migration {
    fn name(&self) -> &str {
        "m20250301_000001_snippet"
    }
}

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        manager
            .create_table(
                Table::create()
                    .table(Snippet::Table)
                    //.col(ColumnDef::new(Snippet::).string().not_null())
                    .col(
                        ColumnDef::new(Snippet::Id)
                            .integer()
                            .not_null()
                            .auto_increment()
                            .primary_key(),
                    )
                    .col(
                        ColumnDef::new(Snippet::Content)
                            .string()
                            .not_null()
                            .unique_key(),
                    )
                    .col(ColumnDef::new(Snippet::Version).string().not_null())
                    .col(ColumnDef::new(Snippet::Active).boolean().not_null())
                    .col(ColumnDef::new(Snippet::Name).string().not_null().unique_key())
                    .col(ColumnDef::new(Snippet::Type).string().not_null())
                    .to_owned(),
            )
            .await
    }

    async fn down(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        manager
            .drop_table(Table::drop().table(Snippet::Table).to_owned())
            .await
    }
}

#[derive(Iden)]
pub enum Snippet {
    Table,
    Id,

    //<
    Content,
    Version,
    Active,
    Name,
    Type,
}
