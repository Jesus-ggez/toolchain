use diesel::prelude::*;

diesel::table! {
    projects (id) {
        id -> Integer,
        entrypoints -> Text,
        commands -> Text,
        r#type -> Text,
        langs -> Text,
        name -> Text,
        env -> Text,
    }
}


