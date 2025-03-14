from .create_template import create_template
from .create_project import create_project
from .use_template import use_template
from .use_project import use_project

data: dict = {
    'new': {
        'snippet': create_template,
        'project': create_project,

    },
    'use': {
        'snippet': use_template,
        'project': use_project,
    }
}
