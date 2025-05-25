diesel::table! {
    snippets (id) {
        id -> Integer,
        content -> Text,
        name -> Text,
    }
}

diesel::table! {
    projects (id) {
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

