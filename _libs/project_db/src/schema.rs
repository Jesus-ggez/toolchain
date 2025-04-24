diesel::table! {
    snippet (id) {
        id -> Integer,
        content -> Text,
        name -> Text,
    }
}

diesel::table! {
    project (id) {
        id -> Integer,
        composition -> Text,
        entrypoints -> Text,
        commands -> Text,
        version -> Text,
        langs -> Text,
        name -> Text,
        env -> Text,
    }
}

