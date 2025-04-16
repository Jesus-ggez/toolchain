diesel::table! {
    snippet (id) {
        id -> Integer,

        active -> Bool,
        version -> Text,
        content -> Text,
        type_ -> Text,
        name -> Text,
    }
}

