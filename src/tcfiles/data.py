#.?
from .blank_project import blank_project
from .blank_snippet import blank_snippet

#<·
data_templates: dict = {
    'snippet': {
        '_': blank_snippet,
    },
    'project': {
        '_': blank_project,
    }
}
