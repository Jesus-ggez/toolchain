from src import (
    create_template,
    create_project,
    use_template,
    use_project,
    replace,
)

core_fn: dict = {
    'project': use_project,
    'make': create_project,
    'use': use_template,
}

tool_fn: dict = {
    'add': create_template,
    'replace': replace,
}
